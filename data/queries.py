from data import data_manager


def get_shows():
    return data_manager.execute_select(
        'SELECT id, title, year, runtime, rating, trailer, homepage FROM shows LIMIT 15;')


def get_show_genre_ids_by_series_id(movie_id):
    genre_ids = data_manager.execute_select(
        'SELECT name AS genre FROM show_genres JOIN genres ON show_genres.genre_id = genres.id WHERE show_id = %('
        'movie_id)s LIMIT 1',
        {'movie_id': movie_id})
    try:
        return genre_ids[0]
    except IndexError:
        return {'genre': 'unknown'}
