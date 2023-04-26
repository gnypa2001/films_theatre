from flask import Flask, render_template

app = Flask("Film theatre")

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/')
def all_films():
    return render_template("all_films.html")

app.run(debug=True)