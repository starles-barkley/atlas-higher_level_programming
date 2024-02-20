-- Display all genres of a selected show
SELECT tv_genres.name FROM tv_genres
WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name;
