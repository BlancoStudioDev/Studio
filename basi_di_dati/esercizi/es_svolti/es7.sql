create or replace procedure id_plot(movie_id varchar, new_plot text)
	language plpgsql
	as $$
	begin
		perform 1 from imdb.movie where movie.id = movie_id;
		
		if not found then
			raise notice 'Film % non trovato', movie_id;
		else
			update imdb.movie set plot = new_plot where movie.id = movie_id;
			raise notice 'Plot aggiornata';
		end if; 
	end;
$$;
	

CALL id_plot('1234', 'Nuovo plot di prova');

create or replace procedure conta_attore(person_id varchar)
	language plpgsql
	as $$
	
	declare conteggio integer;
	
	begin
		
		select count(distinct crew.movie) into conteggio
		from imdb.crew
		where crew.person = person_id and crew.p_role = 'actor';
	
		if conteggio > 10 then
			raise notice 'Attore prolifico';
			commit;
		else
			raise notice 'Attore non prolifico';
			rollback;
		end if;
	end;
$$;

call conta_attore('0000033');



-- Trova le persone che hanno lavorato come 'actor' in film di ogni genere 
-- assegnato a film prodotti negli USA.

select person.given_name
from imdb.person
where not exists (
	select distinct genre.genre
	from imdb.genre
	join imdb.produced on produced.movie = genre.movie
	where produced.country = 'USA'
	
	except
	
	select distinct g2.genre
	from imdb.genre g2
	join imdb.crew on crew.movie = g2.movie
	where crew.person = person.id and crew.p_role = 'actor'
)


-- Trova i film con il numero di rating più basso (minimo assoluto, non zero — solo tra i film che hanno almeno un rating)

select movie.official_title
from imdb.rating
join imdb.movie on movie.id = rating.movie
order by rating.score asc
limit 1


with score_movie as (
	select rating.score as score, movie.official_title as titolo
	from imdb.movie
	join imdb.rating on rating.movie = movie.id
)
select *
from score_movie
where score = (select min(score) from score_movie) 


-- chi è il più produttivo dei registi?

with conteggio as (
	select distinct person.given_name, count(distinct crew.movie) as counter
	from imdb.person
	join imdb.crew on crew.person = person.id
	where crew.p_role = 'director'
	group by person.given_name
)
select *
from conteggio
where counter = (select max(counter) from conteggio)

-- Hitchcock è il più fottuto produttivo regista

-- Trova i film che hanno lo stesso numero di rating del film con id = '0074512' (Marnie), escludendo Marnie stesso dal risultato.

select movie.official_title, rating.score
from imdb.movie
join imdb.rating on rating.movie = movie.id
where rating.score = (select rating.score from imdb.rating where rating.movie = '0074512')


-- Trova le persone che hanno lavorato in esattamente 2 ruoli diversi (non di più, non di meno) — es. solo 'actor' 
-- e 'director', ma non anche 'producer'.

select distinct person.given_name
from imdb.person
join imdb.crew on crew.person = person.id
group by person.given_name
having count(distinct crew.p_role) = 2

select count(distinct crew.p_role)
from imdb.person
join imdb.crew on crew.person = person.id
where person.given_name = 'Aaron Sorkin'


-- Trova i generi assegnati a film con score medio superiore alla media generale di tutti gli score medi dei film.

with score as (
	select avg(rating.score) as media_per_genere, genre.genre
	from imdb.genre 
	join imdb.rating on rating.movie = genre.movie
	group by genre.genre
)
select genre
from score
where media_per_genere > (select avg(media_per_genere) as media from score)


select avg(rating.score) as media_per_genere, genre.genre
	from imdb.genre 
	join imdb.rating on rating.movie = genre.movie
	group by genre.genre


-- Trova le persone che hanno lavorato come 'director' in almeno 2 film con lo stesso genere (es. ha diretto 2 o più film di tipo 'Horror').

select distinct person.given_name
from imdb.person
join imdb.crew on person.id = crew.person
join imdb.genre on crew.movie = genre.movie
where crew.p_role = 'director'
group by person.given_name, genre.genre
having count(distinct crew.movie) >= 2


-- Trova i cinema che hanno proiettato film diretti dalla stessa persona in almeno 2 occasioni diverse (cioè un cinema che ha 
-- mostrato almeno 2 film diversi diretti dallo stesso director).

select cinema.name, person.given_name
from imdb.cinema
join imdb.show on show.cinema_name = cinema.name
join imdb.crew on crew.movie = show.movie 
join imdb.person on person.id = crew.person
where crew.p_role = 'director'
group by cinema.name, person.given_name
having count(distinct crew.movie) >= 2


select *
from imdb.show


-- Trova i generi che non sono mai stati assegnati a nessun film diretto da '0000033'

select distinct genre.genre
from imdb.genre
where not exists (
	select 1
	from imdb.crew
	join imdb.genre g2 on g2.movie = crew.movie
	where genre.genre = g2.genre
	and crew.p_role = 'director'
	and crew.person = '0000033'
)

-- Trova i film che non sono mai stati prodotti (produced) in 'USA' o 'ITA'.

select movie.official_title
from imdb.movie
where movie.id not in (
	select produced.movie
	from imdb.produced
	where produced.country = 'USA'
	
	union
	
	select produced.movie
	from imdb.produced
	where produced.country = 'ITA'
)

-- oppure

select movie.official_title
from imdb.movie
where movie.id not in (
	select produced.movie
	from imdb.produced
	where produced.country = 'USA' or produced.country = 'ITA'
)


select movie.official_title
from imdb.movie
join imdb.produced on produced.movie = movie.id
where produced.country <> 'ITA' and produced.country <> 'USA'


