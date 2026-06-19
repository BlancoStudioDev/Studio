create or replace function conta_film(nome_attore varchar)
	returns integer as $$
	declare 
		conteggio integer;
	begin
			select count(*) into conteggio
			from imdb.crew 
			join imdb.person on person.id = crew.person
			where person.given_name = nome_attore and crew.p_role = 'actor';

			if conteggio is null then
				return 0;
			else
				return conteggio;
			end if;
	end;
$$ language plpgsql;
	
select conta_film('Tom Cruise');

create or replace function lunghezza_film(nome_film varchar)
	returns integer as $$
	declare
		lunghezza integer;
	begin
			select movie.length into lunghezza
			from imdb.movie
			where movie.official_title = nome_film;
			if lunghezza is null then
				return 0;
			else
				return lunghezza;
			end if;			
	end;
$$ language plpgsql;

select lunghezza_film('Marnie');
	

create or replace function nome_caps(id_attore varchar)
	returns varchar as $$
	declare
		nome_maiuscolo varchar;
	begin
		select initcap(person.given_name) into nome_maiuscolo
		from imdb.person
		where person.id = id_attore;
		
		return nome_maiuscolo;
	end;
$$ language plpgsql;

select nome_caps('0000033');

create or replace function valori_film(id_movie varchar)
	returns varchar as $$
	declare
		stringa_formattata varchar;
	begin
		select concat('"', movie.official_title,'" ', '(', movie.year, ')', ' ', movie.length, ' min') into stringa_formattata
		from imdb.movie
		where movie.id = id_movie;
		
		return stringa_formattata;
	end;
$$ language plpgsql;
		
select valori_film('0074512');

select movie.id, movie.official_title, movie.year, movie.length
from imdb.movie;

create or replace function anni(id_actor varchar)
	returns varchar as $$
	declare
		birth date;
		death date;
	begin
		select person.birth_date, person.death_date into birth, death
		from imdb.person
		where person.id = id_actor;

		if death is null then
			return cast(2026 - cast(extract(year from birth) as integer) as integer)-1;
		else
			return cast((cast(extract(year from death) as integer) - cast(extract(year from birth) as integer))as integer);		
		end if;
	end;
$$ language plpgsql;

select anni('0923839');

select *
from imdb.person;

create or replace function data_rilascio(movie_id varchar)
	returns varchar as $$
	declare
		data_release varchar;
	begin
		select to_char(released.released, 'DD/MM/YYYY') into data_release
		from imdb.released
		where released.movie = movie_id and released.country = 'ITA';
		
		return data_release;	
	end;
$$ language plpgsql;
	
select data_rilascio('0074512');

create or replace function prova(movie_id varchar)
	returns table(paese varchar, data varchar) as $$
	begin
		return query
		select released.country::varchar, to_char(released.released, 'DD/MM/YYYY')::varchar
		from imdb.released
		where movie_id = released.movie;

	end;
$$ language plpgsql;

select prova('0074512');


select *
from imdb.released
where released.movie = '0074512';

create or replace function generi(genere varchar)
	returns table(titolo varchar, anno integer) as $$
	begin
		return query
		select movie.official_title::varchar, movie.year::integer
		from imdb.movie
		join imdb.genre on movie.id = genre.movie
		where genre.genre = genere;
	end;
$$ language plpgsql;

select generi('Drama');		

create or replace function genere(drama varchar)
	returns void as $$
	declare
		film imdb.movie%rowtype;
	begin
		for film in
			select *
			from imdb.movie
			join imdb.genre on genre.movie = movie.id
			where genre.genre = drama
		loop
			raise notice 'Titolo: %', film.official_title;
			raise notice 'Anno: %', film.year;		
		end loop;
	end;
$$ language plpgsql;

select genere('Drama');


create or replace function genere_tabella(drama varchar)
	returns table(titolo varchar, anno integer) as $$
	declare
		film imdb.movie%rowtype;
	begin
		for film in
			select *
			from imdb.movie
			join imdb.genre on genre.movie = movie.id
			where genre.genre = drama
		loop
			titolo := film.official_title;
			anno := film.year;
			return next;
		end loop;
	end;
$$ language plpgsql;

select genere_tabella('Drama');		

create or replace function nome_film(movie_id varchar)
	returns varchar as $$
	declare
		nome varchar;
	begin
		select movie.official_title into nome
		from imdb.movie
		where movie.id = movie_id;
		if not found then
			return 'non esiste';
		else
			return nome;
		end if;
	end;
$$ language plpgsql;

select nome_film('0074512');


CREATE OR REPLACE FUNCTION check_anno()
    RETURNS TRIGGER AS $$
    BEGIN
        IF NEW.official_title = 'gay' THEN
            RAISE EXCEPTION 'Impossibile inserire il film: anno % maggiore di 2026', NEW.year;
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER anno_film
    BEFORE INSERT ON imdb.movie
    FOR EACH ROW
    EXECUTE FUNCTION check_anno();

insert into imdb.movie(id, year, official_title)
values('1234567', 2028, 'porn');

delete from imdb.movie
where movie.id = '1234567'

insert into imdb.movie(id, year, official_title)
values('1234567', 2012, 'gay');

select *
from imdb.movie

create or replace function check_delete_movie()
returns trigger as $$
	begin
		raise exception 'non puoi eliminare gay';
		return old;
	end;
$$ language plpgsql;

create trigger gay_non_eliminare_movie
	before delete on imdb.movie
	for each row
	execute function check_delete_movie();
	
delete from imdb.movie
where movie.id = '1234567'

create or replace function check_update_movie()
	returns trigger as $$
	begin
		if new.official_title = '' then
			raise exception 'non puoi fare update con una stringa vuota ricchione';			
		else
			return new;
		end if;
	end;	
$$ language plpgsql;

create trigger no_update_empty
	before update on imdb.movie
	for each row
	execute function check_update_movie();

UPDATE imdb.movie SET official_title = '' WHERE id = '0074512';

select rating.score
from imdb.rating

create or replace function check_score_0_10()
	returns trigger as $$
	begin
		if new.score not between 0 and 10 then
			raise exception 'lo score è sbagliato... non puoi inserire';
		else
			return new;
		end if;
	end;
$$ language plpgsql;

create trigger check_score
	before insert on imdb.rating
	for each row
	execute function check_score_0_10();

INSERT INTO imdb.rating(check_date, source, movie, scale, votes, score)
VALUES(NOW(), 'IMDb', '0074512', 100, 1000, 150);


create or replace function check_person_crew_match()
	returns trigger as $$
	begin
		perform * from imdb.person where new.person = person.id;
		if not found then
			raise exception 'stai sbagliando ad inserire';
		else
			return new;
		end if;
	end;
$$ language plpgsql;

create trigger check_person_crew
	before insert on imdb.crew
	for each row
	execute function check_person_crew_match();
	
INSERT INTO imdb.crew(person, movie, p_role)
VALUES('9999999', '0074512', 'actor');

INSERT INTO imdb.crew(person, movie, p_role)
VALUES('0000033', '0074512', 'actor');













