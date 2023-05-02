from flask import Flask, render_template
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
    return render_template("index.html")

@app.route('/all_films')
def all_films():
    return render_template("all_films.html", spisok = get_spisok())

@app.route('/horror')
def horrors():
    return render_template("horror.html", spisok = get_spisok())

@app.route('/comedy')
def comedy():
    return render_template("comedy.html", spisok = get_spisok())

@app.route('/action')
def action():
    return render_template("action.html", spisok = get_spisok())


app.run(debug=True)