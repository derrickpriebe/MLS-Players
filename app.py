from flask import Flask, jsonify, render_template, json, redirect, request
import pandas as pd 

# Flask constructor
app = Flask(__name__)

# Data setup
table = pd.read_csv("salaries.csv")
table.fillna('', inplace=True)
table_dict = {col: list(table[col]) for col in table.columns}
headings = list(table.columns)
data = list(table.values)[0:10]
print(data[0])

# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)

@app.route('/GetPlayerInfo/<int:rowindex>')
def get_player_info(rowindex):
    return jsonify(list(data[rowindex]))

@app.route('/search/', methods=["POST"])
def search():
    #print(request.form.get)
    name = request.form.get("name")
    print(name)
    team = request.form.get("team")
    print(team)
    filterdata = []
    return render_template("home.html", headings=headings, data=filterdata)

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)