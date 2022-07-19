from flask import Flask, render_template, json, redirect, request
import pandas as pd 
 
# Flask constructor
app = Flask(__name__)
 
# Data setup
salary_table = pd.read_csv("salaries.csv")
salary_table.fillna('', inplace=True)
headings = list(salary_table.columns)
print(headings)
data = list(salary_table.values)
print(data)

# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)

@app.route('/GetPlayerInfo/<row>')
def GetPlayerInfo(row):
    return row + "something"

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)