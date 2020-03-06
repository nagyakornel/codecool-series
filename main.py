from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    try:
        pagenum = int(request.args['p'])
        sortby = request.args['o']
        direction = request.args['d']
        shows = queries.get_shows(pagenum, sortby, direction)
        if direction == "asc":
            direction = "desc"
        else:
            direction = "asc"
    except KeyError or ValueError:
        try:
            pagenum = int(request.args['p'])
            shows = queries.get_shows(pagenum)
            sortby = "rating"
            direction = "asc"
        except KeyError or ValueError:
            shows = queries.get_shows()
            pagenum = 0
            sortby = "rating"
            direction = "asc"
    for show in shows:
        genre_dict = queries.get_show_genre_ids_by_series_id(show['id'])
        show['genre'] = []
        for genre in genre_dict:
            show['genre'].append(genre['genre'])
    return render_template('index.html', shows=shows, pagenum=pagenum, direction=direction)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/show/<show_id>')
def show_page(show_id):
    details = queries.get_show_details(show_id)
    details = details[0]
    details['trailer'] = details['trailer'].replace('watch?v=', 'embed/')
    try:
        details['trailer'].replace('watch?v=', 'embed/')
    except TypeError:
        pass
    details['genre'] = []
    genre_dict = queries.get_show_genre_ids_by_series_id(show_id)
    for genre in genre_dict:
        details['genre'].append(genre['genre'])
    seasons = queries.get_seasons_by_show_id(show_id)
    return render_template('show.html', seasons=seasons, details=details)


@app.route('/pa/1/1')
def pa_1_1():
    shows = queries.get_all_shows_with_episode_nums()
    for show in shows:
        if int(show['count']) >= 100:
            show['is_long'] = True
        else:
            show['is_long'] = False

    return render_template('pa.1.1.html', shows=shows)


@app.route('/pa/1/2')
def pa_1_2():
    actors = queries.get_10_most_played_actors()
    sum_of_plays = 0
    for actor in actors:
        sum_of_plays += int(actor['count'])
    return render_template('pa.1.2.html', actors=actors, count=sum_of_plays)
    print()


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
