from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    # allow the server to keep reloading
    app.debug = True

    # conntect to the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

else:
    app.debug = False

# prevent the warming message
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# define the database model
class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200), unique = True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    # constructor
    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

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

        # prevent user from submitting twice
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)

            # add the data to the database
            db.session.add(data)

            # save the changes
            db.session.commit()

            send_mail(customer, dealer, rating, comments)

            return render_template("success.html")

        return render_template("index.html", message="You have already submitted")

if __name__ == "__main__":
    # run the server
    app.run()