-- Selects shows from database with no associated genre
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
