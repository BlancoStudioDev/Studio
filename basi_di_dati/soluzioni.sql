-- Soluzione 01
select *
from imdb.movie 


-- Soluzione 02
select id as "movie id", year, official_title as title   
from imdb.movie;


-- Soluzione 03
select id, official_title, year
from imdb.movie 
where year = '2010';


-- Soluzione 04
select id, official_title, year
from imdb.movie 
where year <> '2010';


-- Soluzione 05
SELECT *
from imdb.person 
where given_name = 'Leonardo DiCaprio';


-- Soluzione 06
SELECT *
from imdb.person 
where given_name = 'leonardo diCaprio';


-- Soluzione 07
SELECT *, lower(given_name) as "lower name", char_length(given_name)
from imdb.person 
where lower(given_name) = 'leonardo dicaprio';


-- Soluzione 08
select *
from imdb.person 
where birth_date = '1974-11-11';


-- Soluzione 09
select *
from imdb.person 
where birth_date >= '1974-01-01' and birth_date <= '1974-12-31';


-- Soluzione 10
select *
from imdb.person 
where birth_date between '1974-01-01' and '1974-12-31';


-- Soluzione 11
select id, given_name, birth_date, to_char(birth_date, 'DD/MM/YYYY') as it_birth_date, extract(year from birth_date)::text as birth_year
from imdb.person 
where extract(year from birth_date)::text = '1974';


-- Soluzione 12
select *
from imdb.movie
where length >= 60 and length <= 120

select *
from imdb.movie
where length between 60 and 120


-- Soluzione 13
select *
from imdb.movie
where length > 60 and length < 120 and year > '2010'


-- Soluzione 14
select *
from imdb.movie
where year > '2010' or (length > 60 and length < 120)

select *
from imdb.movie
where length > 60 and length < 120 or year > '2010'


-- Soluzione 15
select *
from imdb.movie
where year = '2011' or year = '2013' or year = '2015'

select *
from imdb.movie
where year IN ('2011', '2013', '2015');


-- Soluzione 16
select *
from imdb.person 
where death_date is null 


-- Soluzione 17
select *
from imdb.person 
where death_date is not null 

select * from imdb.movie


-- Soluzione 18
select * from imdb.movie where year = '2010'


-- Soluzione 19
select * from imdb.movie where year <> '2010'
select * from imdb.movie where not (year = '2010')


-- Soluzione 20
select * from imdb.movie where year is null


-- Soluzione 21
select *
from imdb.movie 
where lower(official_title) like '%murder%'


-- Soluzione 22
select *
from imdb.movie 
where lower(official_title) like 'murder%'


-- Soluzione 23
select *
from imdb.movie 
where lower(official_title) like '%murder'


-- Soluzione 24
select *
from imdb.movie 
where plot ilike '%murder%'


-- Soluzione 25
select *
from imdb.movie 
where plot ilike '% murder %'


-- Soluzione 26
update imdb.movie set official_title = ' Marnie' where id = '0058329'


-- Soluzione 27
select * 
from imdb.movie 
where trim(official_title) = 'Marnie'


-- Soluzione 28
select *
from imdb.perso
where extract(year from birth_date)::text = '1980'
order by given_name desc


-- Soluzione 29
select *
from imdb.person 
where extract(year from birth_date)::text = '1980'
order by birth_date [asc], given_name desc


-- Soluzione 30
select *
from imdb.genre 
where genre = 'Thriller'


-- Soluzione 31
select *
from imdb.genre, imdb.movie 


-- Soluzione 32
select *
from imdb.genre, imdb.movie 
where genre.movie = movie.id 


-- Soluzione 33
select *
from imdb.genre inner join imdb.movie on genre.movie = movie.id 


-- Soluzione 34
select movie.id, movie.official_title
from imdb.genre, imdb.movie 
where genre.movie = movie.id and genre = 'Thriller'

select movie.id, official_title
from imdb.genre inner join imdb.movie on genre.movie = movie.id 
where genre = 'Thriller'


-- Soluzione 35
select movie.id, official_title
from imdb.genre inner join imdb.movie on genre.movie = movie.id 
where genre = 'Thriller'
order by official_title 


-- Soluzione 36
select p.id, p.given_name, "character", m.official_title, p_role  
from imdb.person p, imdb.crew c, imdb.movie m
where p.id=c.person and c.movie=m.id and m.official_title ilike 'inception' and p_role = 'actor'
order by character

select p.id, p.given_name, "character", m.official_title, p_role  
from imdb.person p inner join imdb.crew c on p.id=c.person inner join imdb.movie m on c.movie=m.id 
where m.official_title ilike 'inception' and p_role = 'actor'
order by character


-- Soluzione 37
select *
from imdb.genre g 
where genre = 'Thriller' and genre = 'Comedy'


-- Soluzione 38
select *
from imdb.genre g 
where genre = 'Thriller' or genre = 'Comedy'
order by movie


-- Soluzione 39
select *
from genre gt, genre gc 
where gt.genre = 'Thriller' and gc.genre = 'Comedy' and gt.movie=gc.movie 

select gt.movie 
from genre gt inner join genre gc on gt.movie=gc.movie
where gt.genre = 'Thriller' and gc.genre = 'Comedy'


-- Soluzione 40
select g.movie 
from genre g 
where g.genre = 'Thriller' and g.movie in
(select  g.movie
from genre g 
where g.genre = 'Comedy');


-- Soluzione 41
select g.movie 
from genre g 
where g.genre = 'Thriller' 
intersect
select g.movie 
from genre g 
where g.genre = 'Comedy'


-- Soluzione 42
select movie.id, movie.official_title 
from genre gt inner join genre gc on gt.movie=gc.movie inner join imdb.movie on gc.movie=movie.id 
where gt.genre = 'Thriller' and gc.genre = 'Comedy'


-- Soluzione 43
select g.movie, movie.id, official_title 
from genre g inner join imdb.movie on g.movie=movie.id 
where g.genre = 'Thriller' and g.movie in
(select  g.movie
from genre g 
where g.genre = 'Comedy');


-- Soluzione 44
select g.movie, official_title 
from genre g inner join imdb.movie on g.movie=movie.id 
where g.genre = 'Thriller' 
intersect
select g.movie, official_title 
from genre g inner join imdb.movie on g.movie=movie.id 
where g.genre = 'Comedy'


-- Soluzione 45
select official_title 
from genre g inner join imdb.movie on g.movie=movie.id 
where g.genre = 'Thriller' 
intersect
select official_title 
from genre g inner join imdb.movie on g.movie=movie.id 
where g.genre = 'Comedy'


movie
=====
id  | official_title
=====================
001		M1
002		M1

genre
======
movie | genre
=============
001		Thriller
002     Comedy 


-- Soluzione 46
select id, official_title 
from imdb.movie inner join imdb.produced on movie = id 
where country = 'USA';


-- Soluzione 47
select distinct country, name 
from imdb.movie inner join imdb.released on movie = id inner join imdb.country on country = iso3
where year = '2010'
order by country; 


-- Soluzione 48
select distinct country, name, official_title, title  
from imdb.movie inner join imdb.released on movie = id inner join imdb.country on country = iso3
where year = '2010'
order by country; 


-- Soluzione 49
select *
from imdb.location l_birth, imdb.location l_death
where l_birth.d_role = 'B' and l_death.d_role = 'D' and l_birth.person = l_death.person and l_birth.country <> l_death.country; 

select *
from imdb.location l_birth inner join imdb.location l_death on l_birth.person = l_death.person
where l_birth.d_role = 'B' and l_death.d_role = 'D' and  l_birth.country <> l_death.country; 


-- Soluzione 50
select id, given_name, l_birth.country, l_death.country
from imdb.location l_birth inner join imdb.location l_death on l_birth.person = l_death.person inner join imdb.person on person.id = l_birth.person   
where l_birth.d_role = 'B' and l_death.d_role = 'D' and  l_birth.country <> l_death.country; 


-- Soluzione 51
with country_different as (
select l_birth.person, l_birth.country as country_birth, l_death.country as country_death  
from imdb.location l_birth inner join imdb.location l_death on l_birth.person = l_death.person
where l_birth.d_role = 'B' and l_death.d_role = 'D' and  l_birth.country <> l_death.country)
select given_name, country_different.*
from imdb.person inner join country_different on person.id = country_different.person 


-- Soluzione 52
with p_birth as (
select person, country 
from imdb.location 
where d_role = 'B'),
p_death as (
select person, country 
from imdb.location 
where d_role = 'D'),
country_different as (
select p_birth.person, p_birth.country as birth_country,  p_death.country as death_country
from p_birth inner join p_death on p_birth.person = p_death.person 
where p_birth.country <> p_death.country)
select given_name, country_different.*
from imdb.person inner join country_different on person.id = country_different.person ; 


-- Soluzione 53
create view imdb.movie_genre as (
select *
from imdb.movie inner join imdb.genre on movie = id);


-- Soluzione 54
select id, official_title
from imdb.movie_genre
where genre = 'Thriller';


-- Soluzione 55
select id 
from imdb.movie 
except 
select distinct movie
from imdb.material 


-- Soluzione 56
explain analyze 
select movie
from imdb.material 

explain analyze 
select distinct movie
from imdb.material 

explain analyze 
select id 
from imdb.movie 
except 
select movie
from imdb.material

explain analyze 
select id 
from imdb.movie 
except 
select distinct movie
from imdb.material


-- Soluzione 57
select id 
from imdb.movie 
where id not in  
(select distinct movie
from imdb.material)


-- Soluzione 58
select *
from imdb.movie left outer join imdb.material on movie.id = material.movie 
where material.movie is null


-- Soluzione 59
select distinct movie 
from imdb.text inner join imdb.material on material.id = text.material 
union  
select movie 
from imdb.multimedia inner join imdb.material on material.id = multimedia.material 
where type ='image'
order by movie


-- Soluzione 60
select distinct movie 
from imdb.text inner join imdb.material on material.id = text.material 
intersect  
select movie 
from imdb.multimedia inner join imdb.material on material.id = multimedia.material 
where type ='image'
order by movie


-- Soluzione 61
with movie_image as (
select movie 
from imdb.multimedia inner join imdb.material on material.id = multimedia.material 
where type ='image'),
movie_text as (
select distinct movie 
from imdb.text inner join imdb.material on material.id = text.material)
select mi.movie 
from movie_image mi inner join movie_text mt on mi.movie = mt.movie; 


-- Soluzione 62
select  iso3
from imdb.country 
except 
select country  
from imdb.produced 


-- Soluzione 63
select  iso3, name 
from imdb.country   
except 
select country, name  
from imdb.produced inner join imdb.country on country = iso3 


-- Soluzione 64
with no_productions as (
select  iso3
from imdb.country 
except 
select country  
from imdb.produced
)
select country.iso3, name 
from imdb.country inner join no_productions on country.iso3 = no_productions.iso3


-- Soluzione 65
with no_productions as (
select  iso3
from imdb.country 
except 
select country  
from imdb.produced
)
select country.iso3, name 
from imdb.country natural join no_productions 


-- Soluzione 66
select  iso3, name 
from imdb.country 
where iso3 not in (
select country  
from imdb.produced);


-- Soluzione 67
select * 
from imdb.country c left join imdb.produced p on c.iso3 = p.country 
where movie is null; 


-- Soluzione 68
select * 
from imdb.produced p right join imdb.country c on c.iso3 = p.country 
where movie is null;


-- Soluzione 69
explain analyze
select *
from imdb.country c
where not exists (
select * 
from imdb.produced p
where p.country = c.iso3);


-- Soluzione 70
produced  
========
movie | country
===============
001		ITA
002		ITA * 
001		USA 


-- Soluzione 71
select * 
from imdb.produced m_ita left join imdb.produced n_ita on m_ita.movie = n_ita.movie
where m_ita.country = 'ITA' and n_ita.country <> 'ITA' and n_ita.movie is null;


-- Soluzione 72
select * 
from imdb.produced m_ita left join imdb.produced n_ita on m_ita.movie = n_ita.movie and n_ita.country <> 'ITA'
where m_ita.country = 'ITA' and n_ita.movie is null;


-- Soluzione 73
movie | country | movie | country
=================================
001		ITA		  001		ITA 
001		ITA		  002		ITA
001		ITA		  001		USA 
002		ITA		  001		ITA
002		ITA		  002		ITA
002		ITA		  001		USA 
001		USA		  001		ITA
001		USA		  002		ITA
001		USA		  001		USA 


-- Soluzione 74
movie | country | movie | country
=================================
001		ITA		  001		USA 
001		USA		  001		USA


-- Soluzione 75
movie | country | movie | country
=================================
001		ITA		  001		USA 
001		USA		  001		USA
002		ITA 


-- Soluzione 76
with m_ita as (
select *
from imdb.produced 
where country = 'ITA'
), n_ita as (
select *
from imdb.produced 
where country <> 'ITA')
select *
from m_ita left join n_ita on m_ita.movie = n_ita.movie
where n_ita.movie is null; 

m_ita
=====
movie | country 
================
001		ITA
002		ITA

n_ita
movie | country 
================
001		USA

m_ita left join n_ita on m_ita.movie = n_ita.movie
movie | country | movie | country
=================================
001		ITA			001		USA
002		ITA 


-- Soluzione 77
select movie
from imdb.produced 
where country = 'ITA'
except
select movie
from imdb.produced 
where country <> 'ITA'


-- Soluzione 78
with thrillers as (
select *
from imdb.genre g 
where genre = 'Thriller'
)
select r.*
from imdb.rating r inner join thrillers t on t.movie = r.movie
order by score/scale desc
limit 1


-- Soluzione 79
with thrillers as (
select *
from imdb.genre g 
where genre = 'Thriller'
), thrillers_rating as (
select rating.*, score/scale as evaluation
from imdb.rating natural join thrillers),
thrillers_non_max as (
select distinct tr2.*
from thrillers_rating tr1 inner join thrillers_rating tr2 on tr1.evaluation > tr2.evaluation)
select *
from thrillers_rating
except 
select *
from thrillers_non_max;


-- Soluzione 80
with thrillers as (
select *
from imdb.genre g 
where genre = 'Thriller'
), thrillers_rating as (
select rating.*, score/scale as evaluation
from imdb.rating natural join thrillers),
thrillers_non_max as (
select distinct tr2.*
from thrillers_rating tr1 inner join thrillers_rating tr2 on tr1.evaluation > tr2.evaluation)
select tr.*
from thrillers_rating tr left join thrillers_non_max tn on tr.movie = tn.movie 
where tn.movie is null;


-- Soluzione 81
with thrillers as (
select *
from imdb.genre g 
where genre = 'Thriller'
), thrillers_rating as (
select rating.*, score/scale as evaluation
from imdb.rating natural join thrillers)
SELECT tr1.*
FROM thrillers_rating tr1
WHERE NOT EXISTS (
    SELECT *
    FROM thrillers_rating tr2 
    WHERE tr2.evaluation > tr1.evaluation
);


-- Soluzione 82
-- (Soluzione da completare)


