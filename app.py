from flask import Flask, render_template, json, redirect, request
 
# Flask constructor
app = Flask(__name__)
 
# Homepage URL call
@app.route("/")
def home():
    return render_template("home.html")
 
# Listener
if __name__ == "__main__":
    app.run(port=2509, debug=True)