from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    make_response
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
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {user_name}, have a good day!")
    return render_template("about.html", title="About")


@app.route("/contact")
def contact():
    user_name = request.cookies.get("user_name")
    if user_name is None:
        flash("Login Required!")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {user_name}, have a good day!")
    return render_template("contact.html", title="Contact")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        response = make_response("")
        response.set_cookie("user_name", user_name)
        flash(f"Successfully logged in as {user_name.title()}!")
        next_url = request.args.get("next") or url_for("home")
        response.headers["Location"] = next_url
        response.status_code = 302
        return response
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)