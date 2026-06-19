set SEARCH_PATH to imdb;

select score, movie.id, movie.official_title
from imdb.movie join imdb.rating on rating.movie = movie.id
where movie.official_title like '%nception%';

create or replace function get_movie_top_rating(varchar(200))
returns numeric as $$
declare
    top_rating imdb.rating.score%TYPE;
begin
    select max(score)
    into top_rating
    from imdb.rating
    inner join imdb.movie on movie.id = rating.movie
    where movie.official_title like $1;

    return top_rating;
end;
$$ language plpgsql;

select * from get_movie_top_rating('Inception');
select * from get_movie_top_rating('');

select score, movie.id, movie.official_title
from imdb.movie join imdb.rating on rating.movie = movie.id
where movie.id = '0025452';


-- get_movie_genre
-- Data il titolo di un film, restituisce i generi associati
-- input: il titolo di un film
-- output: SETOF di generi associati ai film con titolo considerato

create or replace function get_movie_genre(varchar(200)) returns setof imdb.genre as $$
begin
	return query
	select genre.*
	from imdb.genre inner join imdb.movie on movie.id = genre.movie where movie.official_title ilike $1; 

end;
$$ language plpgsql;

select * from get_movie_genre('%inception%');

set SEARCH_PATH to imdb;

create or replace function get_movie_genre_loop(varchar(200)) returns setof imdb.genre as $$
declare a_genre imdb.genre%rowtype;
begin
	for a_genre in select genre.* from imdb.genre inner join imdb.movie on movie.id = genre.movie where movie.official_title ilike $1 loop
		return next a_genre;
	end loop;
	return;
end;
$$ language plpgsql;

select * from get_movie_genre_loop('%inception%');

		

