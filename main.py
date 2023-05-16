from flask import Flask, render_template, make_response, request, redirect, url_for
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

@app.route('/watch', methods = ["POST"])
def add_watchlist():
    resp = make_response(redirect(url_for("main_page")))
    print(request.form['film_name'])
    resp.set_cookie("watch_later", request.form['film_name'])
    return resp


@app.route('/watch_later')
def watch_later():
    with open("films.json", "r") as file:
        temp = json.load(file)
    spisok = []
    for name in temp:
        if name == request.cookies.get("watch_later"):
            spisok.append(Film(name, temp[name]['link'], temp[name]['descr'], temp[name]['genre']))
    if "login" in request.cookies:
        return render_template("watch_later.html", log = request.cookies.get("login"), spisok = spisok)
    
    return render_template("watch_later.html", log = "log-in", spisok = spisok)


@app.route('/register')
def registration():
    return render_template("register.html")

@app.route('/register_validation', methods = ["POST"])
def register_validation():
    with open("logins.json", "r") as file:
        temp = json.load(file)

    if request.form['username'] not in temp:
        temp[request.form['username']] = request.form['password']
    
    with open("logins.json", "w") as file:
        json.dump(temp, file, indent=4)
        
    return redirect(url_for('main_page'))

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_validation', methods = ["POST"])
def login_validation():
    with open("logins.json", "r") as file:
        temp = json.load(file)

    for login in temp:
        if login == request.form['username'] and temp[login] == request.form['password']:
            resp = make_response(redirect(url_for("main_page")))
            resp.set_cookie("login", request.form['username'])
            return resp
        
    return redirect(url_for('login'))

@app.route('/')
def main_page():
    if "login" in request.cookies:
        return render_template("index.html", log = request.cookies.get("login"))
    return render_template("index.html", log = "log-in")


@app.route('/all_films')
def all_films():
    if "login" in request.cookies:
        return render_template("film_by_genre.html", log = request.cookies.get("login"), spisok = get_spisok())
    return render_template("film_by_genre.html", log = "log-in", spisok = get_spisok())

@app.route('/horror')
def horrors():
    horror = []
    for film in get_spisok():
        if(film.genre == "horror"):
            horror.append(film)
    if "login" in request.cookies:
        return render_template("film_by_genre.html", log = request.cookies.get("login"), spisok = horror)

    return render_template("film_by_genre.html", log = "log-in", spisok = horror)

@app.route('/comedy')
def comedy():
    comedy = []
    for film in get_spisok():
        if(film.genre == "comedy"):
            comedy.append(film)
    if "login" in request.cookies:
        return render_template("film_by_genre.html", log = request.cookies.get("login"), spisok = comedy)
    
    return render_template("film_by_genre.html", log = "log-in", spisok = comedy)

@app.route('/action')
def action():
    action = []
    for film in get_spisok():
        if(film.genre == "action"):
            action.append(film)
    if "login" in request.cookies:
        return render_template("film_by_genre.html", log = request.cookies.get("login"), spisok = action)

    return render_template("film_by_genre.html", log = "log-in", spisok = action)

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for("main_page")))
    resp.set_cookie("login", "log-in")
    resp.delete_cookie('watch_later')
    return resp

app.run(debug=True)
