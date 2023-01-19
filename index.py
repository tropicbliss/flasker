from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/book"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model: any):
    __tablename__ = "book"

    isbn13: str = db.Column(db.String(13), primary_key=True)
    title: str = db.Column(db.String(64), nullable=False)
    price: float = db.Column(db.Float(precision=2), nullable=False)
    availability: int = db.Column(db.Integer)

    def __init__(self, isbn13: str, title: str, price: float, availability: int):
        self.isbn13 = isbn13
        self.title = title
        self.price = price
        self.availability = availability

    def json(self):
        return {"isbn13": self.isbn13, "title": self.title, "price": self.price, "availability": self.availability}


@app.get("/book")
def get_all():
    booklist = Book.query.all()
    pass


@app.route("/book/<string:isbn13>")
def find_by_isbn13(isbn13):
    pass


@app.post("/book/<string:isbn13>")
def create_book(isbn13):
    pass


if __name__ == "__main__":
    app.run(port=5000, debug=True)
