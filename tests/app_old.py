from flask import Flask, render_template, json, redirect, request
import pandas as pd 
 
# Flask constructor
app = Flask(__name__)
 
# Data setup
salary_data = pd.read_csv("salaries.csv")

# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/home_copy', methods=("POST", "GET"))
def table():

    return render_template('home_copy.html',  tables=[salary_data.to_html(classes='data')], titles=salary_data.columns.values)

# Homepage URL call - J2 file
@app.route("/home")
def home1():
    return render_template("home.j2")

# Results URL call
@app.route("/results.html")
def results():
    return render_template("/results.html")

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)