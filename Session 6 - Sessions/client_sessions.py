from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    session,
    request
)
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    if "user_name" not in session:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {session["user_name"]}, have a good day!")
    return render_template("about.html", title="About")


@app.route("/contact")
def contact():
    if "user_name" not in session:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {session["user_name"]}, have a good day!")
    return render_template("contact.html", title="Contact")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session["user_name"] = form.username.data
        flash(f"Successfully logged in as {session["user_name"].title()}!")
        next_url = request.args.get("next")
        return redirect(next_url or url_for("home"))
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)