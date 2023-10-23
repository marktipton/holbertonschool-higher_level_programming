-- download dumpfile with data about tv shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- match rows from tv_show_genres where the id in tv_shows
-- matches the show_id in tv_show_genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;