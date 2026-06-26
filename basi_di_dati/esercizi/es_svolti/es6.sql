with tot_film as (
	select count(distinct crew.movie) as numero_film, crew.person
	from imdb.crew
	join imdb.movie on crew.movie = movie.id
	where crew.p_role = 'actor' and movie.year > '1990'
	group by crew.person
)
select distinct tot_film.person, numero_film 
from tot_film
where numero_film > (select avg(numero_film) from tot_film)

select *
from imdb.crew

-- Trova il genere con il maggior numero di film prodotti (produced) in un singolo paese specifico (es. 'USA').

with film_genere as (
	select count(genre.movie) as generi, genre.genre as genere
	from imdb.genre
	join imdb.produced on produced.movie = genre.movie
	where produced.country = 'USA'
	group by genre.genre
	order by count(genre.movie) desc
)
select genere, generi 
from film_genere
where generi = (select max(generi) from film_genere)


-- Trova le persone che hanno lavorato come 'actor' in film di almeno 3 generi diversi 
-- (cioè un attore "versatile", che ha recitato in commedie, drammi, thriller, ecc. — non 
-- necessariamente nello stesso film, ma nell'insieme di tutti i suoi film).

select distinct crew.person, count(genre.genre)
from imdb.crew
join imdb.genre on genre.movie = crew.movie
where crew.p_role = 'actor'
group by crew.person
having count(distinct genre.genre) >= 3

-- Trova i cinema che proiettano film di un solo genere (cioè cinema "specializzati", che non hanno mai mostrato film di generi diversi).

select show.cinema_name, count(distinct genre.genre)
from imdb.show
join imdb.genre on genre.movie = show.movie
group by show.cinema_name
having count(distinct genre.genre) > 1

-- Trova i film che hanno lo stesso identico cast di un altro film (cioè le stesse persone esatte, indipendentemente dal ruolo)
-- — escludendo il confronto di un film con se stesso.

Soggetto esterno = film
soggetto A = tutti i partecipanti al film m1
Soggetto B = tutte i partecipanti al film m2

select m1.official_title, m2.official_title
from imdb.movie m1
join imdb.movie m2 on m1.id <> m2.id
where not exists (
	select crew.person 
	from imdb.crew
	where crew.movie = m1.id
	
	except
	
	select crew.person
	from imdb.crew
	where crew.movie = m2.id
) and not exists (
	select crew.person
	from imdb.crew
	where crew.movie = m2.id
	
	except
	
	select crew.person
	from imdb.crew
	where crew.movie = m1.id
) and m1.id < m2.id


-- Trova la persona (o le persone) che hanno il maggior numero di film come 'actor'.

with conteggio_film as (
	select person.id as codice, count(crew.movie) as conteggio
	from imdb.crew
	join imdb.person on person.id = crew.person
	where crew.p_role = 'actor'
	group by person.id
)
select codice, conteggio
from conteggio_film
where conteggio = (select max(conteggio) from conteggio_film)

select person.given_name as codice, count(crew.movie) as conteggio
from imdb.crew
join imdb.person on person.id = crew.person
where crew.p_role = 'actor'
group by person.given_name
order by count(crew.movie) desc 
limit 1

-- Trova i generi assegnati a meno di 3 film in totale.

select genre.genre, count(genre.movie)
from imdb.genre
group by genre.genre
having count(genre.movie) <= 3


-- Inserisci un nuovo film con id = '9999999', official_title = 'Test Movie', year = 2025

insert into imdb.movie(id, official_title, year)
values('9999999', 'Test Movie', '2025')

update imdb.movie
set plot = 'tutti scemi'
where id = '9999999'

delete from imdb.movie where id = '9999999'


select distinct p1.given_name, p2.given_name, count(c1.movie)
from imdb.crew c1
join imdb.crew c2 on c1.movie = c2.movie
join imdb.person p1 on p1.id = c1.person
join imdb.person p2 on p2.id = c2.person and p1.id < p2.id
where c1.p_role = 'actor' and c2.p_role = 'actor'
group by p1.given_name, p2.given_name
having count(c1.movie) > 1


-- Scrivi una funzione che prende in input un p_role e restituisce, tramite RAISE NOTICE, il numero 
-- totale di persone distinte che hanno quel ruolo, seguito dal nome di ciascuna persona.

create or replace function totale_p_role(ruolo varchar)
	returns void as $$
	declare
		persone varchar;
		conteggio integer;
	begin
		select distinct count(crew.person) into conteggio
		from imdb.person
		join imdb.crew on person.id = crew.person
		where ruolo = crew.p_role;

		for persone in
			select distinct person.given_name
			from imdb.person
			join imdb.crew on crew.person = person.id
			where crew.p_role = ruolo
		loop
			raise notice '%: %', ruolo, persone;
		end loop;
		
		raise notice 'Totale %: %', ruolo, conteggio;

	end;
$$ language plpgsql; 

select totale_p_role('actor')


select count(crew.person)
from imdb.person
join imdb.crew on person.id = crew.person
where crew.p_role = 'actor'
group by crew.p_role


-- Trova i generi che sono stati assegnati a tutti i film diretti da '0000033' (Hitchcock).

select genre.genre
from imdb.genre
where not exists(
	select crew.movie
	from imdb.crew
	where crew.person = '0000033' and crew.p_role = 'director'

	except
	
	select g2.movie
	from imdb.genre g2
	join imdb.crew on g2.movie = crew.movie
	where crew.person = '0000033' and crew.p_role = 'director' and
	g2.genre = genre.genre	
)



-- Aggiorna il plot di tutti i film che non hanno nessun genere assegnato, impostandolo a 'Genere da definire'.

select distinct movie.official_title, genre.genre
from imdb.genre
join imdb.movie on genre.movie = movie.id
where genre.genre is null


update imdb.genre
set genre.genre = 'Genere da definire'
where genre.genre is null

-- Trova i film con almeno 2 rating registrati (in imdb.rating) che hanno uno score medio inferiore a 5.

select movie.official_title
from imdb.rating
join imdb.movie on movie.id = rating.movie
group by movie.official_title
having count(*) >= 2 and avg(rating.score) < 5


-- Crea una funzione che prende in input un id di film e restituisce TRUE se quel film ha più generi della 
-- media (rispetto a tutti i film), FALSE altrimenti.

create or replace function true_false(movie_id varchar)
	returns boolean as $$
	declare
		conteggio integer;
		media_generi float;
	begin
		with media as (
			select count(genre.genre) as score, movie.id
			from imdb.genre
			join imdb.movie on movie.id = genre.movie
			group by movie.id
		)
		select avg(score) into media_generi
		from media;
		
		select count(genre.genre) into conteggio
		from imdb.genre
		where genre.movie = movie_id;
		
		if conteggio > media_generi then
			raise notice 'Vero';
			return true;
		end if;
		raise notice 'Falso';
		return false;
	end;
$$ language plpgsql;

select true_false('6914094');

select movie.id, count(genre.genre)
from imdb.movie
join imdb.genre on genre.movie = movie.id
where movie.id = '6914094'
group by movie.id

with media as (
	select count(genre.genre) as score, movie.id
	from imdb.genre
	join imdb.movie on movie.id = genre.movie
	group by movie.id
	)
select avg(score) as  media_generi
from media

select movie.id
from imdb.movie


-- Trova le persone che hanno lavorato in ogni film che ha vinto/ha un rating con score >= 9 (

select person.given_name
from imdb.person
where not exists (
	select rating.movie
	from imdb.rating
	where rating.score >= 9
	
	except
	
	select crew.movie
	from imdb.rating
	join imdb.crew on crew.movie = rating.movie
	where rating.score >= 9 and crew.person = person.id
)


-- Scrivi una query che mostra, per ogni cinema, il nome del primo film (in ordine alfabetico) che ha mai proiettato.

select min(movie.official_title), cinema.name
from imdb.movie
join imdb.show on show.movie = movie.id
join imdb.cinema on cinema.name = show.cinema_name
group by cinema.name


select min(movie.official_title)
from imdb.movie
join imdb.show on show.movie = movie.id
join imdb.cinema on cinema.name = show.cinema_name
where cinema.name = 'PALESTRINA'


-- Trova le persone che hanno lavorato come 'director' in film usciti in almeno 3 decenni diversi 
-- (es. una persona che ha diretto film negli anni '60, '70 e '80).

select crew.person
from imdb.movie
join imdb.crew on crew.movie = movie.id
where crew.p_role = 'director'
group by crew.person
having count(distinct (cast(movie.year as integer) / 10) * 10) >= 3


select movie.year
from imdb.movie
join imdb.crew on crew.movie = movie.id
where crew.person = '0000040'
order by movie.year


-- Trova i film che hanno un solo genere assegnato, mostrando titolo e quel genere.

with codice_film as (
	select movie.id as codice
	from imdb.genre
	join imdb.movie on movie.id = genre.movie
	group by movie.id
	having count(genre.genre) = 1
)
select movie.official_title, genre.genre
from imdb.movie
join imdb.genre on genre.movie = movie.id
join codice_film on codice = movie.id

select genre.genre
from imdb.movie
join imdb.genre on genre.movie = movie.id
where movie.official_title = 'Sabbia'


-- Trova il numero totale di film per ogni p_role esistente in crew 
-- (es. quanti film hanno almeno un 'actor', quanti hanno almeno un 'director', ecc.)

select crew.p_role, count(distinct movie.id)
from imdb.crew
join imdb.movie on movie.id = crew.movie
group by crew.p_role 

select crew.p_role, count(distinct crew.movie)
from imdb.crew
group by crew.p_role 


-- Trova i film che hanno lo stesso anno di uscita e lo stesso numero di generi assegnati di almeno un altro film.

with film_genere_anno as (
	select movie.year, genre.genre
	from imdb.movie
	join imdb.genre on movie.id = genre.movie
)


select movie.year, genre.genre
from imdb.movie
join imdb.genre on movie.id = genre.movie


-- Trova le coppie di paesi (country) che hanno prodotto film insieme (cioè esiste almeno un film prodotto da entrambi 
-- i paesi contemporaneamente, secondo la tabella produced).

select distinct p1.country, p2.country
from imdb.produced p1
join imdb.movie m1 on p1.movie = m1.id
join imdb.produced p2 on p1.movie = p2.movie and p1.country < p2.country


-- Trova i film che hanno lo stesso director di un film con score (rating) medio superiore a 8.

with direttore_score as (
	select distinct crew.person as direttore
	from imdb.rating
	join imdb.crew on crew.movie = rating.movie
	where rating.score > 8 and crew.p_role = 'director'
)
select distinct movie.official_title
from direttore_score
join imdb.crew on crew.person = direttore
join imdb.movie on movie.id = crew.movie


-- Si restituiscano le coppie di persone che hanno diretto e recitato nello stesso film (adattamento di "padre-figlio" 
-- come relazione tra due persone collegate da un evento comune).

select p1.given_name, p2.given_name
from imdb.crew c1
join imdb.crew c2 on c1.person <> c2.person and c1.movie = c2.movie
join imdb.person p1 on c1.person = p1.id
join imdb.person p2 on c2.person = p2.id
where c1.p_role = 'director' and c2.p_role = 'actor'


-- Per ogni persona, si restituisca il numero di film in cui ha lavorato come 'actor'. Si includano nel risultato anche le persone 
-- che non hanno mai recitato (compariranno con conteggio zero)

select distinct person.given_name, count(crew.movie)
from imdb.person
left join imdb.crew on person.id = crew.person and crew.p_role = 'actor'
group by person.given_name


-- Si restituisca la persona (o le persone) che ha lavorato nel maggior numero di ruoli diversi (p_role distinti).

with person_ruoli as (
	select distinct person.given_name, count(distinct crew.p_role) as conteggio
	from imdb.crew
	join imdb.person on person.id = crew.person
	group by person.given_name
)
select *
from person_ruoli
where conteggio = (select max(conteggio) from person_ruoli) 


-- Si restituiscano le persone che non hanno mai lavorato in nessun film (cioè non sono presenti in crew).

select distinct person.given_name, crew.p_role
from imdb.person
left join imdb.crew on crew.person = person.id
where crew.person is null


-- Individuare le persone che hanno lavorato in tutti i diversi ruoli disponibili in crew.

select person.given_name
from imdb.person
where not exists (
	select crew.p_role
	from imdb.crew
	
	except
	
	select crew.p_role
	from imdb.crew
	where crew.person = person.id
)










