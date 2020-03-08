from data import data_manager


def get_shows(offset=0, sortby='rating', direction='asc'):
    offset *= 15
    return data_manager.execute_select(
        'SELECT id, title, year, runtime, rating, trailer, homepage FROM shows ORDER BY '
        + sortby + ' ' + direction +
        ' LIMIT 15 OFFSET %(offset)s',
        {'sortby': sortby, 'direction': direction, 'offset': offset})


def get_show_genre_ids_by_series_id(movie_id):
    genre_ids = data_manager.execute_select(
        'SELECT name AS genre FROM show_genres FULL JOIN genres ON show_genres.genre_id = genres.id WHERE show_id = %('
        'movie_id)s LIMIT 3',
        {'movie_id': movie_id})
    try:
        return genre_ids
    except IndexError:
        return {'genre': 'unknown'}


def get_characters_by_show(show_id):
    return data_manager.execute_select(
        'SELECT character_name, name '
        'FROM show_characters RIGHT JOIN actors a on show_characters.actor_id = a.id '
        'WHERE show_id = %(show_id)s',
        {'show_id': show_id})


def get_seasons_by_show_id(show_id):
    return data_manager.execute_select(
        'SELECT season_number, title, overview '
        'FROM seasons '
        'WHERE show_id = %(show_id)s',
        {'show_id': show_id}
    )


def get_show_details(show_id):
    return data_manager.execute_select(
        'SELECT id, title, year, runtime, rating, trailer, homepage, overview FROM shows '
        'WHERE id = %(show_id)s',
        {'show_id': show_id}
    )


def get_all_shows_with_episode_nums():
    return data_manager.execute_select(
        'SELECT shows.title, COUNT(s.show_id), COUNT(e.season_id) '
        'FROM shows JOIN seasons s on shows.id = s.show_id '
        'JOIN episodes e on s.id = e.season_id '
        'GROUP BY shows.title;'
    )


def get_10_most_played_actors():
    return data_manager.execute_select(
        'SELECT actors.name, COUNT(sc.actor_id) '
        'FROM actors JOIN show_characters sc on actors.id = sc.actor_id '
        'GROUP BY actors.name '
        'ORDER BY COUNT(sc.actor_id) DESC '
        'LIMIT 10;'
    )


def get_all_shows_with_minimum_episodes(episodes):
    return data_manager.execute_select(
        'SELECT shows.title, COUNT(s.show_id), COUNT(e.season_id), genres.name '
        'FROM shows JOIN seasons s on shows.id = s.show_id '
        'JOIN episodes e on s.id = e.season_id '
        'JOIN show_genres on shows.id = show_genres.show_id '
        'JOIN genres on show_genres.genre_id = genres.id '
        'GROUP BY genres.name, shows.title '
        'HAVING COUNT(s.show_id) >= %(episodes)s ',
        {'episodes': episodes}
    )


def get_all_shows_with_minimum_seasons(seasons):
    return data_manager.execute_select(
        'SELECT shows.title, COUNT(s.show_id), genres.name '
        'FROM shows JOIN seasons s on shows.id = s.show_id '
        'JOIN show_genres on shows.id = show_genres.show_id '
        'JOIN genres on show_genres.genre_id = genres.id '
        'GROUP BY genres.name, shows.title '
        'HAVING COUNT(s.show_id) >= %(seasons)s ',
        {'seasons': seasons}
    )


def get_show_ids_by_genre(genre):
    return data_manager.execute_select(
        'SELECT shows.title, shows.year, shows.rating '
        'FROM shows JOIN show_genres sg on shows.id = sg.show_id '
        'JOIN genres g on sg.genre_id = g.id '
        'WHERE g.name LIKE %(genre)s '
        'ORDER BY shows.rating DESC '
        'LIMIT 10',
        {'genre': genre}
    )


def get_show_ratings_by_years():
    return data_manager.execute_select(
        'SELECT shows.year, AVG(shows.rating), COUNT(*) '
        'FROM shows '
        "WHERE shows.year BETWEEN '1970-01-01' AND '2010-01-01' "
        'GROUP BY shows.year '
        'ORDER BY shows.year ASC;'
    )
