from flask import Flask

# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return "<h1>Welcome to the Home Page!</h1>"


# about page
@app.route("/about")
def about():
	return "<h1>Welcome to the About Page!</h1>"


# example of path parameter
@app.route("/welcome/<name>")
def welcome(name):
	return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"


# example of integer path parameter
@app.route("/addition/<int:num>")
def addition(num):
	return f"<h1>Input is {num}, Output is {num + 10}</h1>"


# example of two integer path parameters
@app.route("/addition_two/<int:num1>/<int:num2>")
def addition_two(num1, num2):
	return f"<h1>{num1} + {num2} is {num1 + num2}</h1>"


# start the app
if __name__ == "__main__":
	app.run(debug=True)