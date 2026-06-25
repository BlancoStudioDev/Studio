-- Trova il nome di tutte le persone che hanno lavorato sia come 'actor' che come 'director' (in film diversi o nello stesso, non importa).

select distinct person.given_name, c1.p_role, c2.p_role
from imdb.person
join imdb.crew c1 on person.id = c1.person
join imdb.crew c2 on c1.person = c2.person
where c1.p_role = 'actor' and c2.p_role = 'director'

-- Per ogni cinema, conta quanti show (proiezioni) ha programmato. Mostra anche i cinema con zero show.

select cinema.name, count(show.movie)
from imdb.show
join imdb.cinema on show.cinema_name = cinema.name
group by cinema.name

-- Trova i film che non hanno nessun rating registrato in imdb.rating.

select distinct movie.official_title, rating.score
from imdb.movie
join imdb.rating on movie.id = rating.movie
where rating.score is not null

-- Trova, per ogni decennio (es. anni '70, '80, '90...), il numero di film usciti e il budget medio.

select count(movie.official_title) as num_film, (cast(year as integer) / 10) * 10 as decennio
from imdb.movie
where movie.year is not null
group by (cast(year as integer) / 10)*10
order by decennio

-- Trova le coppie di film (sim.movie1, sim.movie2) che hanno una cause di similarità in comune con almeno un altro 
-- film, mostrando quanti film condividono quella cause.

select sim.movie1, count(sim.movie2)
from imdb.sim
join imdb.movie on movie.id = sim.movie1
group by sim.movie1
order by count(sim.movie2) desc


select distinct person.given_name, crew.p_role
from imdb.person
join imdb.crew on crew.person = person.id
where person.given_name not in (
	select person.given_name
	from imdb.person
	join imdb.crew on crew.person = person.id
	where crew.p_role = 'actor' 
)


with recursive prova as (
	select 1970 as n
	union all
	select n + 1 from prova where n < 2026
)
select *
from prova;

with recursive prova_film as (
	select movie.id as codice, 0 as salti
	from imdb.movie 
	where movie.id = '0074512'
	union all
	select sim.movie2 as codice, prova_film.salti + 1 as salti
	from imdb.movie
	join imdb.sim on sim.movie1 = movie.id 
	join prova_film on prova_film.codice = sim.movie1
	where prova_film.salti < 1 and movie.id = movie1
)
SELECT distinct * FROM prova_film;

with recursive film_lavorato as (
	select distinct crew.person as codice_person, 0 as salti, crew.movie as codice_film
	from imdb.crew
	where crew.person = '0000033'
	union all
	select distinct crew.person as codice_person, film_lavorato.salti + 1 as salti, crew.movie as codice_film
	from imdb.crew 
	join film_lavorato on film_lavorato.codice_film = crew.movie
	where salti < 3
)
select distinct *
from film_lavorato;

-- Trova tutte le persone che hanno recitato (p_role = 'actor') in almeno un film prodotto (produced) negli Stati 
-- Uniti ('USA'), mostrando nome e titolo del film

select distinct person.given_name, movie.official_title
from imdb.crew
join imdb.person on person.id = crew.person
join imdb.produced on produced.movie = crew.movie
join imdb.movie on crew.movie = movie.id
where crew.p_role = 'actor' and produced.country = 'USA'


-- Per ogni paese in country, calcola il rating medio dei film che ha prodotto. Mostra solo i paesi con rating medio superiore a 7.

select avg(rating.score), produced.country
from imdb.rating
join imdb.produced on produced.movie = rating.movie
group by produced.country
having avg(rating.score) > 7


-- Trova i film che hanno più di un genere assegnato, mostrando titolo e numero di generi.

select count(genre.genre), movie.official_title
from imdb.genre
join imdb.movie on movie.id = genre.movie
group by movie.official_title
having count(genre.genre) > 1


-- Trova le persone che sono sia in crew con ruolo 'director' sia con ruolo 'actor' nello stesso identico film 
-- (quindi hanno diretto e recitato nel medesimo film).

select distinct person.given_name, c1.p_role, c2.p_role
from imdb.crew c1
join imdb.crew c2 on c1.person = c2.person and c1.movie = c2.movie
join imdb.person on person.id = c1.person
where c1.p_role = 'actor' and c2.p_role = 'director'


-- Scrivi una funzione che prende in input un id di una persona e restituisce, tramite RAISE NOTICE, tutti i 
-- film in cui ha lavorato con il relativo ruolo, ordinati per anno crescente.

create or replace function persona_films(person_id varchar)
	returns void as $$
	declare
		film imdb.movie%rowtype;
	begin
		for film in
			select distinct on (movie.id) movie.*
			from imdb.movie
			join imdb.crew on crew.movie = movie.id
			where crew.person = person_id
			ORDER BY movie.id, movie.year ASC
		loop
			raise notice 'Titolo: %', film.official_title;
		end loop;
	end;
$$ language plpgsql;

select persona_films('0000033');

select crew.person
from imdb.crew


-- Crea un trigger che impedisce di inserire un rating con votes negativo o zero in imdb.rating.

create or replace function trigger_anti_negative_vote()
	returns trigger as $$
	begin
		if new.score < 0 then
			raise exception 'Non puoi inserire uno score negativo';
		end if;
		return new;
	end;
$$ language plpgsql;

drop function trigger_anti_negative_vote();

create trigger voti_negativi
	before insert on imdb.rating
	for each row
	execute function trigger_anti_negative_vote();

insert into imdb.rating(scale,votes,score)
values('-1','-1','-1')


-- Usando una CTE, trova i primi 3 film per score più alto, per ogni decennio.

with decennio as (
	select rating.score, movie.official_title, (cast(year as integer) / 10 ) * 10 as anni, movie.id as movie_id
	from imdb.movie
	join imdb.rating on rating.movie = movie.id
),
ranking AS (
    SELECT *, RANK() OVER (PARTITION BY anni ORDER BY score DESC) AS posizione
    FROM decennio
)
SELECT * FROM ranking WHERE posizione <= 3;

-- Restituire i film con il maggior numero di generi assegnati 

select distinct movie.official_title, count(genre.genre)
from imdb.movie
join imdb.genre on genre.movie = movie.id
group by movie.official_title
order by count(genre.genre) desc
limit 10

with numero_film as (
	select movie.official_title as titolo, count(genre.genre) as numero
	from imdb.movie
	join imdb.genre on genre.movie = movie.id
	group by movie.official_title 
)
select max(numero), numero_film.official_title
from numero_film


-- Trova le coppie di persone che hanno lavorato con lo stesso p_role (es. entrambe 'director') in anni consecutivi, con film diversi

select distinct c1.p_role, c2.p_role, c1.person, c2.person
from imdb.crew c1
join imdb.crew c2 on c1.p_role = c2.p_role
join imdb.movie movie1 on movie1.id = c1.movie
join imdb.movie movie2 on movie2.id = c2.movie
where (cast(movie2.year as integer) + 1) = cast(movie1.year as integer)



select distinct crew.p_role
from imdb.crew 

select person.given_name
from imdb.person
join imdb.crew c1 on c1.person = person.id
join imdb.crew c2 on c2.person = person.id
join imdb.crew c3 on c3.person = person.id
join imdb.crew c4 on c4.person = person.id and c1.person = c2.person and c3.person = c4.person and c2.person = c3.person
where c1.p_role = 'producer' and c2.p_role = 'actor' and c3.p_role = 'director' and c4.p_role = 'writer'
-- questa è la query giusta ma stupida

-- ora facciamo quella corretta ed intelligente

select person.given_name
from imdb.person
where not exists (
	select distinct crew.p_role
	from imdb.crew
	
	except
	
	select distinct crew.p_role
	from imdb.crew 
	where person.id = crew.person
)


-- Restituire il titolo dei film che hanno avuto proiezioni (show) in più di 3 cinema diversi.

select movie.official_title, count(distinct cinema_name)
from imdb.movie
join imdb.show on show.movie = movie.id 
group by movie.official_title 
having count(distinct cinema_name) >= 2

-- Restituire i film che non hanno mai un rating registrato in imdb.rating

select movie.official_title
from imdb.movie
left join imdb.rating on rating.movie = movie.id
where rating.movie is null

-- Restituire le persone che hanno vinto/avuto il rating più alto tra tutti i film in cui hanno lavorato come 'director' 
-- (cioè: trova il director il cui film ha lo score medio più alto in assoluto).


with direttore as (
	select crew.person, crew.movie
	from imdb.crew
	where crew.p_role = 'director'
)
select direttore.person, rating.score
from direttore 
join imdb.rating on rating.movie = direttore.movie
order by rating.score desc
limit 1

with direttore as (
	select crew.person, crew.movie
	from imdb.crew
	where crew.p_role = 'director'
)
select distinct direttore.person, max(rating.score)
from direttore 
join imdb.rating on rating.movie = direttore.movie
group by direttore.person


-- Trova le coppie di film che condividono almeno 2 generi in comune.

select movie.official_title, count(m2.id)
from imdb.genre
join imdb.movie on movie.id = genre.movie
join imdb.genre g2 on genre.genre = g2.genre  
join imdb.movie m2 on m2.id = g2.movie and movie.id <> m2.id
group by movie.official_title
having count(distinct genre.genre) > 2

-- Trova i cinema che hanno proiettato (show) tutti i film usciti dopo il 2000.

select cinema.name
from imdb.cinema
where not exists (
	select movie.id
	from imdb.movie
	where movie.year > '2000'
	
	except
	
	select show.movie
	from imdb.show
	where show.cinema_name = cinema.name
)
	
-- Trova le persone che hanno lavorato (in qualunque ruolo) in tutti i film prodotti negli USA (produced.country = 'USA').

select person.given_name
from imdb.person
where not exists (
	select produced.movie
	from imdb.produced 
	where produced.country = 'USA'
	
	except
	
	select crew.movie
	from imdb.crew
	where crew.person = person.id
)
	
-- Restituire i film che non hanno mai un attore ('actor') nato dopo il 1980 nel cast.

select movie.official_title
from imdb.movie
where not exists (
	select person.id
	from imdb.person
	join imdb.crew on crew.person = person.id
	where movie.id = crew.movie and (extract(year from person.birth_date) > 1980) and crew.p_role = 'actor' 
)

-- Trova i generi che non sono mai stati assegnati a un film prodotto (produced) negli USA.

select distinct genre.genre
from imdb.genre
where not exists (
	select 1
	from imdb.produced
	join imdb.genre g2 on g2.movie = produced.movie
	where genre.genre = g2.genre and produced.country = 'USA'
)


-- Trova i generi che sono stati assegnati a tutti i film diretti da una specifica persona (es. person.id = '0000033', Hitchcock).

select genre.genre
from imdb.genre
where not exists (
	select crew.movie
	from imdb.crew
	where crew.person = '0000033' and crew.p_role = 'director'
	
	except
	
	select g2.movie
	from imdb.crew
	join imdb.genre g2 on g2.movie = crew.movie
	where genre.genre = g2.genre and crew.person = '0000033' and crew.p_role = 'director'
)


select distinct genre.genre
from imdb.crew
join imdb.genre on genre.movie = crew.movie
where crew.p_role = 'director' and crew.person = '0000033'


-- Trova le persone che hanno lavorato (in qualunque ruolo) in tutti i film in cui ha lavorato 
-- anche '0000033' (Hitchcock) — escludendo Hitchcock stesso dal risultato.

select person.given_name
from imdb.person
where not exists (
	select crew.movie
	from imdb.crew
	where crew.person = '0000033'
	
	except
	
	select c2.movie
	from imdb.crew c2
	where person.id = c2.person and c2.person = '0000033'
)
and person.id <> '0000033'


-- Trova i paesi (country) che hanno prodotto (produced) tutti i generi presenti nel database — 
-- cioè un paese che ha prodotto almeno un film per ogni genere esistente

select distinct produced.country
from imdb.produced
where not exists (
	select distinct genre.genre
	from imdb.genre

	except
	
	select g2.genre
	from imdb.genre g2
	join imdb.produced p2 on g2.movie = p2.movie
	where p2.country = produced.country
)

-- Trova le persone che hanno lavorato (in qualunque ruolo) in ogni film in cui ha lavorato anche '0000033' 
-- E in nessun altro film oltre a quelli — cioè persone con esattamente lo stesso 
-- insieme di film di Hitchcock (né più, né meno).

Soggetto esterno -> imdb.person
A -> Film in cui ha lavorato 0000033 crew.movie
B -> Film di persone che hanno lavorato con 0000033

select person.given_name
from imdb.person
where not exists (
	select crew.movie
	from imdb.crew
	where crew.person = '0000033'
	
	except
	
	select c2.movie
	from imdb.crew c2
	where person.id = c2.person
)
and not exists (
	select c2.movie
	from imdb.crew c2
	where person.id = c2.person
	
	except
	
	select crew.movie
	from imdb.crew
	where crew.person = '0000033'
)
and person.id <> '0000033'


-- Trova, per ogni anno, il numero di film usciti e la percentuale che rappresentano sul totale dei film nel database (arrotondata a 2 decimali).

select count(movie.official_title)
from imdb.movie

with anno as (
	select (cast(movie.year as integer) / 1 ) * 1 as annualita, count(movie.official_title) as numeri
	from imdb.movie
	group by cast(movie.year as integer) / 1 * 1
)
select annualita, numeri, round((numeri::numeric / (select sum(numeri) from anno) * 100), 2)
from anno
order by annualita


-- Trova le persone che hanno lavorato in più film come 'director' rispetto al numero medio di film per direttore (cioè i direttori "sopra la media").

with prova as (
	select count(crew.movie) as numeri, crew.person
	from imdb.crew
	where crew.p_role = 'director'
	group by crew.person
)
select distinct crew.person, count(crew.movie)
from imdb.crew
where crew.p_role = 'director'
group by crew.person
having count(crew.movie) > (select avg(numeri) from prova)

select count(crew.movie), crew.person
from imdb.crew
where crew.p_role = 'director'
group by crew.person


-- fare in modo di avere tutti i film con gli score più alti degli score medi del genere a cui appartengono

with score_medio as (
	select avg(rating.score) as media
	from imdb.genre
	join imdb.rating on rating.movie = genre.movie
	where genre.genre = 'Drama'
)
select movie.official_title, rating.score
from imdb.movie
cross join score_medio
join imdb.rating on movie.id = rating.movie
join imdb.genre on genre.movie = movie.id
where rating.score > score_medio.media and genre.genre = 'Drama'


