-- Scrivi una query che estragga il nome del cinema e il titolo del film per tutte le proiezioni

select movie.official_title, show.cinema_name
from imdb.movie join imdb.show on movie.id = show.movie


-- Scrivi una query che estragga il titolo ufficiale del film (movie.official_title) e il numero
-- totale di nazioni in cui è stato prodotto, mostrando solo i film che sono stati prodotti 
-- in almeno 2 nazioni diverse.

select movie.official_title, count(produced.country)
from imdb.movie join imdb.produced on produced.movie = movie.id 
group by official_title
having count(produced.country) >= 2;



-- Scrivi una query che estragga il titolo ufficiale del film (movie.official_title) e il 
-- numero totale di generi a cui appartiene, mostrando solo i film che sono classificati in 
-- almeno 3 generi diversi.

select movie.official_title, count(genre.movie)
from imdb.movie join imdb.genre on movie.id = genre.movie 
group by movie.official_title
having count(genre.genre) >= 3;

-- Scrivi una query per estrarre i titoli ufficiali dei film (movie.official_title)
-- che NON compaiono mai nella tabella delle recensioni.

select movie.official_title
from imdb.movie 
where movie.id not in (
	select rating.movie
	from imdb.rating
)

select movie.official_title 
from imdb.rating join imdb.movie on movie.id = rating.movie

-- Scrivi una query che estragga il titolo ufficiale del film (movie.official_title) 
-- per tutti i film che NON sono mai usciti in Italia (nella tabella released, l'Italia 
-- ha come codice paese 'ITA').

select distinct movie.official_title
from imdb.movie join imdb.released on movie.id = released.movie
where movie.id not in(
	select released.movie
	from imdb.released
	where released.country = 'ITA'
);

select movie.official_title
from imdb.movie join imdb.released on movie.id = released.movie
where released.country = 'ITA'

-- Trova il nome della persona (person.given_name) e l'ID dei registi che hanno diretto 
-- almeno 3 film il cui length (durata) è superiore a 150 minuti.

select distinct person.given_name, person.id
from imdb.person join imdb.crew on person.id = crew.person join imdb.movie on movie.id = crew.movie
where crew.p_role = 'producer' and movie.length > 150
group by person.given_name, person.id
having count(movie.id) >= 3

select *
from imdb.person join imdb.crew on person.id = crew.person join imdb.movie on movie.id = crew.movie
where movie.length > 150

-- Scrivi una query che estragga il titolo ufficiale del primo film e il titolo 
-- ufficiale del secondo film, per tutte le coppie che hanno uno score superiore a 0.8.

select m1.official_title, m2.official_title, sim.score
from imdb.sim join imdb.movie m1 on m1.id = sim.movie1 join imdb.movie m2 on sim.movie2 = m2.id
where sim.score > 0.8


-- nomi dei registi e il nome del paese in cui sono nati, ma solo se il numero di film che hanno
-- diretto è maggiore della media del numero di film diretti dagli altri registi dello stesso paese.



select person.given_name, person.id, location.country as registi_maggiori_avg
from imdb.person join imdb.crew on person.id = crew.person join imdb.location on location.person = person.id
where crew.p_role = 'producer'
group by person.id, person.given_name, location.country
having count(crew.movie) > (
	select avg(num_films)
	from (
		select crew.movie, count(crew.movie) as num_films
		from imdb.person join imdb.crew on crew.person = person.id
		where crew.p_role = 'producer'
		group by crew.movie
	) as media_films
);


-- Trova il nome (given_name) di tutti i registi che hanno diretto esattamente 1 solo film.
-- Inoltre, vogliamo che il titolo ufficiale di quel film sia mostrato accanto al nome del regista.

select max(movie.official_title), person.given_name
from imdb.movie join imdb.crew on crew.movie = movie.id join imdb.person on person.id = crew.person
where crew.p_role = 'producer'
group by person.id, person.given_name
having count(crew.movie) = 1;


-- Trova il nome (given_name) di tutti i registi che hanno diretto almeno un film tra il 1990 
-- e il 1999 E almeno un film dal 2020 al 2026.

with registinovanta as (
	select crew.person
	from imdb.crew join imdb.movie on crew.movie = movie.id
	where crew.p_role = 'producer' and CAST(movie.year AS INTEGER) between 1990 and 1999
),
registiduemila as (
	select crew.person
	from imdb.crew join imdb.movie on crew.movie = movie.id
	where crew.p_role = 'producer' and CAST(movie.year AS INTEGER) between 2020 and 2026
)
select person.given_name
from imdb.crew join imdb.person on person.id = crew.person join registiduemila rd 
	on rd.person = crew.person join registinovanta rn on crew.person = rn.person;


-- colleghi dei colleghi di tom cruise

with Tom_Cruise (
	select distinct crew.movie
	from imdb.person join imdb.crew on crew.person = person.id
	where person.given_name = 'Tom Cruise'
),
colleghi (
	select crew.movie
	from imdb.person
	where movie in (select movie from Tom_Cruise)
)
SELECT DISTINCT p.given_name
FROM imdb.person p
JOIN imdb.crew c ON p.id = c.person
WHERE c.movie IN (SELECT movie FROM FilmDeiColleghi)
  AND p.given_name != 'Tom Cruise';


-- Trova i nomi di due persone (chiamiamole PersonaA e PersonaB) che hanno lavorato 
-- nello stesso film per almeno 5 volte

SELECT 
    p1.given_name AS PersonaA, 
    p2.given_name AS PersonaB, 
    COUNT(*) AS NumeroCollaborazioni
FROM imdb.crew c1
JOIN imdb.crew c2 ON c1.movie = c2.movie AND c1.person < c2.person
JOIN imdb.person p1 ON c1.person = p1.id
JOIN imdb.person p2 ON c2.person = p2.id
GROUP BY p1.given_name, p2.given_name
HAVING COUNT(*) >= 5
ORDER BY NumeroCollaborazioni DESC;


select *
from imdb.crew
where crew.person = '0000794'


-- Vogliamo trovare i nomi dei registi che hanno diretto SOLO film di un 
-- determinato genere (ad esempio 'Drama'), e che non hanno mai diretto nessun altro genere.

select distinct person.given_name
from imdb.genre join imdb.crew on crew.movie = genre.movie join imdb.person on person.id = crew.person
where genre = 'Drama' and crew.p_role = 'producer'

-- così però prendo anche i registi che oltre al drama hanno fatto altro.

select distinct person.given_name
from imdb.genre join imdb.crew on crew.movie = genre.movie join imdb.person on person.id = crew.person
where crew.p_role = 'director' and genre = 'drama' and person.id not in (
	select crew.person
	from imdb.crew join imdb.movie on movie.id = crew.movie join imdb.genre on genre.movie = crew.movie
	where genre.genre <> 'Drama' and crew.p_role = 'director'
);

SELECT count(*) 
FROM imdb.person 
WHERE id IN (SELECT person FROM imdb.crew JOIN imdb.genre ON crew.movie = genre.movie WHERE genre = 'Drama' AND p_role = 'director');


-- diretto almeno 5 film

select person.given_name, movie.length
from imdb.crew join imdb.person on person.id = crew.person join imdb.movie on movie.id = crew.movie
where crew.p_role = 'director'
group by person.given_name, movie.length
having count(crew.movie) >= 5 and movie.length  > (select avg(movie.length) from imdb.movie) 


-- regista con il numero maggiore di film

with maggiore as (
	select crew.person, count(crew.movie) as totale_film
	from imdb.crew
	where crew.p_role = 'director'
	group by crew.person
)
select person.given_name, mg.totale_film
from maggiore mg join imdb.person on mg.person = person.id
where mg.totale_film > 10
order by mg.totale_film desc


-- Vogliamo scoprire, per ogni regista che ha diretto almeno 5 film, qual è il suo genere preferito 
-- (quello in cui ha diretto più film).

with conteggio_generi_regista as (
	select person.given_name, genre.genre, count(genre.genre) as nome_genere_numero, person.id as regista_id
	from imdb.genre join imdb.crew on genre.movie = crew.movie join imdb.person on person.id = crew.person
	where crew.p_role = 'director'
	group by person.given_name, genre.genre, person.id
)
select person.given_name, cgr.genre, cgr.nome_genere_numero 
from conteggio_generi_regista cgr join imdb.person on person.id = cgr.regista_id
where cgr.nome_genere_numero >= 5
order by cgr.nome_genere_numero desc


-- Vogliamo trovare i registi che hanno diretto almeno 3 film nel primo decennio della loro carriera 
-- (i primi 10 anni in cui hanno diretto) e almeno 3 film negli ultimi 10 anni della loro carriera.

select 
from imdb.crew join imdb.person on person.id = crew.person join imdb.movie on crew.movie = movie.id
where crew.p_role = 'director' and (person.birth_date + 30)
and cast(movie.year as integer) between 1990 and 2000


with film_vita as (
	select count(crew.movie) as numero, person.id as nome
	from imdb.crew join imdb.person on person.id = crew.person join imdb.movie on crew.movie = movie.id
	where crew.p_role = 'director' 
	group by person.id
)
select distinct person.given_name, movie.year, person.birth_date 
from film_vita fm join imdb.person on person.id = fm.nome join imdb.crew on crew.person = person.id
join imdb.movie on movie.id = crew.movie
where fm.numero >= 3 and cast(movie.year as integer) between (extract(year from person.birth_date) + 30) and (extract(year from person.birth_date) + 40)


-- trovare i film correlati ad un film dato

with film as (
	select crew.person as persona
	from imdb.movie join imdb.crew on movie.id = crew.movie
	where crew.p_role = 'director' and movie.official_title = 'Family Plot'
	group by crew.person
)
select distinct person.given_name, movie.official_title, crew.p_role
FROM imdb.movie
JOIN imdb.crew ON movie.id = crew.movie join imdb.person on person.id = crew.person
WHERE crew.person IN (SELECT persona FROM film)
  AND crew.p_role = 'director'

  
  
  
-- top 3 registi
  
select person.given_name, count(crew.movie), (cast(movie.year AS INTEGER) / 10) * 10 AS decennio
from imdb.crew join imdb.person on person.id = crew.person join imdb.movie on movie.id = crew.movie
where crew.p_role = 'director'
group by person.given_name, person.id, decennio
having count(crew.movie) >= 5
order by decennio desc, count(crew.movie) desc

  

-- Vogliamo trovare tutti i registi che hanno diretto almeno un film, ma che non hanno mai collaborato
-- con nessun altro regista (cioè nei loro film, nel ruolo di 'director', appaiono sempre da soli).

select *
from imdb.crew c1 join imdb.person on person.id = c1.person
where c1.p_role = 'director' and not exists (
	select 1
	from imdb.crew c2
	where c2.movie = c1.movie and c2.person <> c1.person and c2.p_role = 'director'
);



