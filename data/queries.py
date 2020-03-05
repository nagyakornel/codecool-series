from data import data_manager


def get_shows(offset=0):
    offset *= 15
    return data_manager.execute_select(
        'SELECT id, title, year, runtime, rating, trailer, homepage FROM shows ORDER BY rating DESC LIMIT 15 OFFSET %(offset)s',
        {'offset': offset})


def get_show_genre_ids_by_series_id(movie_id):
    genre_ids = data_manager.execute_select(
        'SELECT name AS genre FROM show_genres FULL JOIN genres ON show_genres.genre_id = genres.id WHERE show_id = %('
        'movie_id)s LIMIT 3',
        {'movie_id': movie_id})
    try:
        return genre_ids
    except IndexError:
        return {'genre': 'unknown'}
