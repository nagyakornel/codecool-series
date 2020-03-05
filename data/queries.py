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
