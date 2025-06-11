from flask import Flask, render_template, url_for
from flaskblog.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "4555225cf5403c4c93dfacdbeb5e28e6"

posts = [
    {
        "author": "Ruairi O'Donohoe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 21, 2018",
    },
    {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")
