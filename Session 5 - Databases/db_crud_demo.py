from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees_db.db"  # URL of DB to establish connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to hide warnings by SQL Alchemy

db = SQLAlchemy(app)

# database models
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, '{self.email}')"

# run the flask app
if __name__ == "__main__":
    app.run(debug=True)