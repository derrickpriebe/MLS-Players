# MLS Player Data Flask Site by Derrick Priebe
# Leveraging Player URL Microservice by Hyunjae Kim
# Oregon State University, CS361 Software Engineering I
# Date: 8/7/2022

from flask import Flask, render_template, redirect, request, url_for
import pandas as pd 
import webbrowser
import zmq

# Flask constructor
app = Flask(__name__)

# Data setup
table = pd.read_csv("salaries.csv")
table.fillna('', inplace=True)
headings = list(table.columns)
data = list(table.values)

# Zeromq setup and socket connection
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)

# Route to get additional player info via "info" link
@app.route('/GetPlayerInfo/<int:rowindex>')
def get_player_info(rowindex):
    # Send and receive message request
    socket.send_string(str(rowindex))
    message = socket.recv_string()
    # Access url from message and open brower tab to resolve url
    webbrowser.open(message)
    return redirect(url_for("home"))

# Route to post search results
@app.route("/", methods=["POST"])
def search():
    search = request.form.get("search")
    name = request.form.get("name")
    name2 = request.form.get("name2")
    team = request.form.get("team")
    filterdata = []
    # Conduct search on data
    for element in data:
        full_search = search == "" or search.lower() in element[0].lower() or \
            search.lower() in element[1].lower() or search.lower() in element[2].lower()
        name_search = name == "" or name.lower() in element[0].lower()
        name2_search = name2 == "" or name2.lower() in element[1].lower()
        team_search = team == "" or team.lower() in element[2].lower()
        if (full_search and name_search and name2_search and team_search):
            filterdata.append(element)
    if filterdata == []:
        # If no search results, show message
        no_data = ["No  "]
        return render_template("home.html", headings=no_data, name=name, name2=name2, team=team)
    else:
        # If search results, show results
        return render_template("home.html", headings=headings, data=filterdata,  name=name, name2=name2, team=team)

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)