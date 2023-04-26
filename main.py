from flask import Flask, render_template

app = Flask("Film theatre")

@app.route('/')
def main_page():
    return render_template("index.html")
app.run(debug=True)