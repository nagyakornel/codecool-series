from flask import Flask, render_template, url_for, request, jsonify
from data import queries
import datetime

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


@app.route('/pa/1/3', methods=['GET', 'POST'])
def pa_1_3():
    if request.method == 'POST':
        seasons = int(request.form.get('seasons'))
        episodes = int(request.form.get('episodes'))
        queried_shows_dict = queries.get_all_shows_with_minimum_episodes(episodes)
        shows_dict = {}
        for show in queried_shows_dict:
            try:
                shows_dict[show['name']] += 1
            except KeyError:
                shows_dict[show['name']] = 1

        queried_shows_dict = queries.get_all_shows_with_minimum_seasons(seasons)
        for show in queried_shows_dict:
            try:
                shows_dict[show['name']] += 1
            except KeyError:
                shows_dict[show['name']] = 1
        return render_template('pa.1.3.html', genres=shows_dict)
    return render_template('pa.1.3.html')


@app.route('/pa/2/1', methods=['GET', 'POST'])
def pa_2_1():
    if request.method == 'POST':
        genre = request.form.get('genre')
        shows = queries.get_show_ids_by_genre(genre)
        return render_template('pa.2.1.html', shows=shows)

    return render_template('pa.2.1.html')


@app.route('/pa/2/2', methods=['GET', 'POST'])
def pa_2_2():
    shows = queries.get_show_ratings_by_years()
    return render_template('pa.2.2.html', years=shows)


@app.route('/pa/2/3', methods=['GET', 'POST'])
def pa_2_3():
    shows = queries.get_top_10_longest_shows()
    actors = {}
    for show in shows:
        show_actors = queries.get_actors_by_show(show['id'])
        for actor in show_actors:
            try:
                actors[actor['name']] += show['id']
            except KeyError:
                actors[actor['name']] = show['id']
    return render_template('pa.2.3.html', shows=shows, actors=actors)


@app.route('/pa/2/4', methods=['GET', 'POST'])
def pa_2_4():
    if request.method == 'POST':
        title = request.form.get('title')
        title = '%' + title + '%'
        results = queries.get_shows_by_title(title)
        for result in results:
            print(result['trailer'])
            try:
                result['trailer'] = result['trailer'].replace('watch?v=', 'embed/')
            except AttributeError:
                pass
        return render_template('pa.2.4.html', results=results)
    return render_template('pa.2.4.html')


@app.route('/pa/2/5', methods=['GET', 'POST'])
def pa_2_5():
    actors = queries.get_characters_age()
    for actor in actors:
        if actor['death'] and actor['birthday']:
            actor['age'] = int(actor['death'] - actor['birthday'])
        if actor['birthday']:
            actor['age'] = int(datetime.date.today() - actor['birthday'])


@app.route('/pa/2/6', methods=['GET', 'POST'])
def pa_2_6():
    if request.method == 'POST':
        date = request.form.get('date') + '-01-01'
        actors = queries.get_actors_born_after_year(date)
        return render_template('pa.2.6.html', results=actors)
    return render_template('pa.2.6.html')


@app.route('/pa/2/7', methods=['GET', 'POST'])
def pa_2_7():
    if request.method == 'POST':
        genre = request.form.get('genre')
        shows = queries.get_all_shows_by_genre(genre)
        return render_template('pa.2.7.html', shows=shows)
    return render_template('pa.2.7.html')


@app.route('/pa/2/8', methods=['GET', 'POST'])
def pa_2_8():
    if request.method == 'POST':
        date = request.form.get('date')
        today = datetime.date.today()
        actors = queries.get_young_actors_by_year(today, date + '-01-01')
        for actor in actors:
            if actor['age_at_release'] > actor['show_age']:
                actor['was_older'] = True
            else:
                actor['was_older'] = False
        return render_template('pa.2.8.html', actors=actors, date=date)
    return render_template('pa.2.8.html')


@app.route('/pa/2/9/')
def pa_2_9():
    return render_template('pa.2.9.html')


@app.route('/search/<search>')
def return_search_value(search):
    complete_search = ''
    i = 0
    while i < len(search) - 1:
        complete_search += f'{search[i]}%'
        i += 1
    complete_search += search[len(search) - 1]
    result = queries.get_characters_by_search_string(complete_search)
    return jsonify(result)


@app.route('/pa/2/10')
def pa_2_10():
    max_num = queries.get_highest_number_of_seasons()[0]['count']
    return render_template('pa.2.10.html', max=max_num)


@app.route('/pa/2/10/api/<num>')
def return_shows(num):
    result = queries.get_shows_by_min_season(int(num))
    return jsonify(result)


@app.route('/pa/2/11')
def pa_2_11():
    genres = queries.get_all_genres()
    return render_template('pa.2.11.html', genres=genres)


@app.route('/pa/api/<genre_id>')
def pa_2_11_get_data(genre_id):
    shows = queries.get_50_shows_by_genre_id(int(genre_id))
    return jsonify(shows)


@app.route('/pa/2/12')
def pa_2_12():
    shows = queries.get_all_shows('shows', 'ASC');
    return render_template('pa.2.12.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
