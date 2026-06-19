-- Trova i titoli ufficiali di tutti i film che appartengono al genere 'Horror'.

select distinct movie.official_title, genre
from imdb.movie join imdb.genre on genre.movie = movie.id
where genre = 'Horror'

-- Elenca i nomi di tutti i registi (person) che hanno lavorato a film prodotti in 'Italy'.

select distinct person.given_name, country, crew.p_role
from imdb.movie 
join imdb.produced on movie.id = produced.movie
join imdb.crew on movie.id = crew.movie 
join imdb.person on crew.person = person.id
where produced.country = 'ITA' and crew.p_role = 'director'

-- Per ogni film, calcola il numero totale di voti ricevuti nella tabella rating. Visualizza
-- il titolo del film e il conteggio totale.

select movie.official_title, SUM(rating.votes) AS totale_voti
from imdb.movie 
join imdb.rating ON movie.id = rating.movie
group by movie.official_title, rating.votes
order by rating.votes desc

-- Trova tutti i film che sono stati proiettati (show) in un cinema situato a 'Milano'. Mostra 
-- il titolo del film, il nome del cinema e l'orario dello spettacolo.

select movie.official_title, show.showtime, cinema.name
from imdb.movie
join imdb.show on movie.id = show.movie
join imdb.cinema on show.cinema_name = cinema.name
where cinema.city = 'Milano'

-- Identifica i film che hanno una somiglianza (sim) con un altro film con un punteggio (score)
-- superiore a 0.8. Visualizza i titoli di entrambi i film.

select distinct m1.official_title, m2.official_title, sim.score 
from imdb.movie m1
join imdb.sim on m1.id = sim.movie1
join imdb.movie m2 on m2.id = sim.movie2
where sim.score > 0.8

-- Trova i titoli di tutti i film che non hanno mai ricevuto alcun voto nella tabella rating.

select *
from imdb.rating

-- Elenca i generi che hanno una media di budget superiore a 50.000.000. Visualizza il nome 
-- del genere e la media del budget.

select movie.budget, genre.genre
from imdb.movie
join imdb.genre on movie.id = genre.movie

-- Trova il nome del regista (person) che ha diretto il maggior numero di film.

select distinct person.given_name, count(movie.id) as numer_film
from imdb.movie
join imdb.crew on crew.movie = movie.id
join imdb.person on crew.person = person.id
group by person.given_name
order by numer_film desc
limit 3


-- Trova tutti i film in cui l'anno di uscita (year nella tabella movie) è diverso dall'anno 
-- in cui il film è stato effettivamente rilasciato in qualche paese (released nella tabella released).
-- Mostra il titolo, l'anno previsto e l'anno effettivo.

select distinct movie.official_title, movie.year, extract(year from released)
from imdb.movie
join imdb.released on movie.id = released.movie
where cast(movie.year as integer) <> cast(extract(year from released.released) as integer)


-- Trova i nomi (given_name) di tutte le persone che hanno lavorato come regista (p_role = 'director') 
-- ma che non hanno mai lavorato come attore (p_role = 'actor') in nessun film presente nel database.

select person.given_name, crew.p_role
from imdb.person 
join imdb.crew on crew.person = person.id
where crew.p_role = 'director' and crew.person not in (
	select crew.person
	from imdb.crew
	where crew.p_role = 'actor'
)

-- Per ogni regista, calcola la differenza di budget tra il suo film più recente e il suo film meno 
-- recente. Visualizza il nome del regista e questa differenza.

select person.given_name
from imdb.movie
join imdb.crew on movie.id = crew.movie
join imdb.person on person.id = crew.person
group by person.given_name
having first_value(movie.year)


-- Vogliamo trovare i registi che hanno diretto almeno 3 film, ma vogliamo solo quelli il cui budget 
-- medio per film è superiore alla media generale di tutti i film presenti nel database.

with maggiori_3 as (
	select crew.person, count(movie) as num_film
	from imdb.crew
	group by crew.person
	having count(crew.movie) > 3
),
score_medio as (
	select avg(rating.score) as media
	from imdb.rating
)
select person.given_name
from imdb.person 
join maggiori_3 mg on mg.person = person.id
cross join score_medio sc
join imdb.crew on crew.person = person.id
join imdb.rating on rating.movie = crew.movie
where crew.p_role = 'director'
group by sc.media, person.id, person.given_name
having sc.media < avg(rating.score);

-- Immagina di voler trovare tutti gli attori che hanno lavorato sia in film del genere 'Action' 
-- sia in film del genere 'Comedy

SELECT DISTINCT p.given_name
FROM imdb.person p
-- Prima JOIN: collega la persona a un film Action
JOIN imdb.crew c1 ON p.id = c1.person
JOIN imdb.genre g1 ON c1.movie = g1.movie AND g1.genre = 'Action'
-- Seconda JOIN: collega la STESSA persona a un film Comedy
JOIN imdb.crew c2 ON p.id = c2.person
JOIN imdb.genre g2 ON c2.movie = g2.movie AND g2.genre = 'Comedy'
WHERE c1.p_role = 'actor' AND c2.p_role = 'actor';

select distinct person.given_name
from imdb.person
join imdb.crew on person.id = crew.person
join imdb.genre on genre.movie = crew.movie
where genre.genre = 'Action' and crew.p_role = 'actor'
intersect
select distinct person.given_name
from imdb.person
join imdb.crew on person.id = crew.person
join imdb.genre on genre.movie = crew.movie
where genre.genre = 'Comedy' and crew.p_role = 'actor';

-- Vogliamo trovare i nomi di tutti i registi (p_role = 'director') che non hanno diretto alcun 
-- film negli ultimi 5 anni (consideriamo come riferimento l'anno corrente: 2026).

select distinct person.given_name
from imdb.person
join imdb.crew on crew.person = person.id
join imdb.movie on movie.id = crew.movie
where crew.p_role = 'director' and crew.person not in (
	select crew.person
	from imdb.movie
	join imdb.crew on movie.id = crew.movie
	where cast(movie.year as integer) > 2021 and crew.p_role = 'director' and person.id = crew.person and movie.year <> Null
);

-- Vogliamo trovare i titoli dei film che hanno ricevuto molti voti (quindi sono stati visti da tante
-- persone), ma che hanno un punteggio (score) molto basso (inferiore alla media globale del database).

with score_medio as (
	select avg(rating.score) as media
	from imdb.rating
)
select movie.id 
from imdb.movie
join imdb.rating on rating.movie = movie.id
cross join score_medio
group by movie.id, score_medio.media
having score_medio.media < avg(rating.score)
intersect
select movie.id
from imdb.movie
join imdb.rating on rating.movie = movie.id
group by movie.id
order by rating.score
limit 100

