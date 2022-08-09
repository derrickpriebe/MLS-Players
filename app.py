# MLS Player Data Flask Site by Derrick Priebe
# Leveraging Player URL Microservice by Hyunjae Kim
# Oregon State University, CS361 Software Engineering I
# Date: 8/7/2022

from flask import Flask, render_template, redirect, request, url_for
import pandas as pd 
import webbrowser
import zmq

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

# Route for homepage
@app.route("/")
def home():
    return render_template("home.html", headings=headings, data=data)

# Route to get additional player info via "info" link
@app.route('/GetPlayerInfo/<int:rowindex>')
def get_player_info(rowindex):
    # Send and receive message request
    socket.send_string(str(rowindex))
    message = socket.recv_string()
    # Access url from message
    webbrowser.open(message)
    return redirect(url_for("home"))

# Function to get inputs from form 
def getInputs(form):
    search = form.get("search")
    name = form.get("name")
    last_name = form.get("last_name")
    team = form.get("team")
    return search, name, last_name, team

# Function to get search criteria for an element
def getSearch(search, name, last_name, team, element, filterdata):
    full_search = search == "" or search.lower() in element[0].lower() or \
        search.lower() in element[1].lower() or search.lower() in element[2].lower()
    name_search = name == "" or name.lower() in element[0].lower()
    last_name_search = last_name == "" or last_name.lower() in element[1].lower()
    team_search = team == "" or team.lower() in element[2].lower()
    if (full_search and name_search and last_name_search and team_search):
            filterdata.append(element)
    return filterdata

# Route to post search results
@app.route("/", methods=["POST"])
def search():
    search, name, last_name, team = getInputs(request.form)
    filterdata = []
    for element in data:
        filterdata = getSearch(search, name, last_name, team, element, filterdata)
    if filterdata == []:
        no_data = ["No  "]
        return render_template("home.html", headings=no_data, name=name, last_name=last_name, team=team)
    else:
        return render_template("home.html", headings=headings, data=filterdata,  name=name, last_name=last_name, team=team)

# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)