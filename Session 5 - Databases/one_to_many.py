from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"  # URL of DB to establish connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to hide warnings by SQL Alchemy

db = SQLAlchemy(app)

# database models
class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False, unique=True)
    state = db.Column(db.String(50), nullable=False)
    members = db.relationship("Player", backref="team")

    def __repr__(self):
        return f"Team('{self.team}', '{self.state}')"
    
class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))

    def __repr__(self):
        return f"Player('{self.name}', '{self.nationality}')"
    

# run the flask app
if __name__ == "__main__":
    app.run(debug=True)