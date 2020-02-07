from flask import Flask, render_template, request

app = Flask(__name__)

# show the home page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        customer = request.form["customer"]
        dealer = request.form["dealer"]
        rating = request.form["rating"]
        comments = request.form["comments"]
        
        # validation 
        if customer == "" or dealer == "":
            return render_template("index.html", message="Make sure you filled out all the fields")

        return render_template("success.html")

if __name__ == "__main__":
    # allow the server to keep reloading
    app.debug = True

    # run the server
    app.run()