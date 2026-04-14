from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

# SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/faridkasdi/mysite/comments.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# -------------------
# DATABASE MODEL
# -------------------
class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


# -------------------
# ROUTE
# -------------------
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        comment_text = request.form["comment"]

        comment = Comment(content=comment_text)
        db.session.add(comment)
        db.session.commit()

    comments = Comment.query.all()

    return render_template("main_page.html", comments=comments)

@app.route("/login/")
def login():
    return render_template("login_page.html")
