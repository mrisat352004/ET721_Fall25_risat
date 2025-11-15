"""
Mahafog Risat
Nov 14, 2025
Lab 12, Introduction to Flask
"""

from flask import Flask, render_template

"""
create an object 'app' from the Flask module.
__name__ set to __main__ if the script is running directly from the main file
"""

app = Flask(__name__)

# set the routing to the main(Loading) page
# 'route' docorator is used to access the root URL
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def qoutes():
    return '<h1>Qoutes</h1>'

# set the 'app' to run if you execute the file directly (not when it is imported)

if __name__ == "__main__":
    app.run(debug=True)
