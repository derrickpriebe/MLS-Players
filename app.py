from flask import Flask
 
# Flask constructor
app = Flask(__name__)
 
# Homepage URL call
@app.route("/")
def home():
    return redirect("/html/home")

@app.route("/html/home")
def Main():
    return render_template("html/home.html")
 
# main driver function
if __name__ == '__main__':
    app.run()