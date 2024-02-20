-- Counts shows in database by genre
SELECT DISTINCT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows FROM tv_genres
