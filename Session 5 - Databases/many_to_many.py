from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"  # URL of DB to establish connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to hide warnings by SQL Alchemy

db = SQLAlchemy(app)

# association table
customer_product = db.Table(
    "customer_product",
    db.Column("customer_id", db.Integer, db.ForeignKey("customers.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"))
)

# database models
class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    items = db.relationship("Product", backref="owners", secondary=customer_product)

    def __repr__(self):
        return f"Customer('{self.name}', '{self.email}')"
    
    
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.product}', '{self.price}')"
    

# run the flask app
if __name__ == "__main__":
    app.run(debug=True)