from flask import Flask, render_template, make_response, request
import json
from film import Film
app = Flask("Film theatre")

def get_spisok():
    with open("films.json", "r") as file:
        temp = json.load(file)
    spisok = []
    for name in temp:
        spisok.append(Film(name, temp[name]['link'], temp[name]['descr'], temp[name]['genre']))
    return spisok


@app.route('/')
def main_page():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("name", "Serhii")
    print(request.cookies.get("prepod"))
    return resp

@app.route('/all_films')
def all_films():
    resp = make_response(render_template("film_by_genre.html", spisok = get_spisok()))
    resp.set_cookie("prepod", "est pichenky")
    return resp

@app.route('/horror')
def horrors():
    horror = []
    for film in get_spisok():
        if(film.genre == "horror"):
            horror.append(film)
    return render_template("film_by_genre.html", spisok = horror)

@app.route('/comedy')
def comedy():
    comedy = []
    for film in get_spisok():
        if(film.genre == "comedy"):
            comedy.append(film)
    return render_template("film_by_genre.html", spisok = comedy)

@app.route('/action')
def action():
    action = []
    for film in get_spisok():
        if(film.genre == "action"):
            action.append(film)
    return render_template("film_by_genre.html", spisok = action)


app.run(debug=True)