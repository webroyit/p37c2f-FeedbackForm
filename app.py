from flask import Flask, render_template, request

app = Flask(__name__)

# define the route
@app.route("/")

# show the home page
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # allow the server to keep reloading
    app.debug = True

    # run the server
    app.run()