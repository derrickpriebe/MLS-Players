from flask import Flask, render_template, json, redirect, request
import pandas as pd 
 
# Flask constructor
app = Flask(__name__)
 
# Data setup
salary_table = pd.read_csv("salaries.csv")
salary_table.fillna('', inplace=True)
headings = list(salary_table.columns)
data = list(salary_table.values)

# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)

@app.route('/GetPlayerInfo/<int:id>')
def GetPlayerInfo(id):
    print('It works! The ID is {id}')
    return redirect('/')

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)