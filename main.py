from flask import Flask, render_template
import json
app = Flask("Film theatre")

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/all_films')
def all_films():
   
    return render_template("all_films.html")

@app.route('/horror')
def horrors():
    return render_template("horror.html")

@app.route('/comedy')
def comedy():
    return render_template("comedy.html")

@app.route('/action')
def action():
    return render_template("action.html")


app.run(debug=True)