from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def home():
    response = make_response("<h1>Welcome to the Home Page!</h1>")
    return response


@app.route("/set_cookie")
def set_cookie():
    response = make_response("<h1>Welcome to the Set Cookie Page!</h1>")
    response.set_cookie("cookie_name", "cookie_value")
    return response


@app.route("/get_cookie")
def get_cookie():
    value = request.cookies.get("cookie_name")
    response = make_response(f"<h1>The cookie value is <i>{value}</i>!</h1>")
    return response


if __name__ == "__main__":
    app.run(debug=True)