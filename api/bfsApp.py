"""
BreathFirstSearch algorithm that is searching
connection-Table to find shortest paths of nodes.
"""
import Models
from app import app 
from db import db


def main():
    db.init_app(app)

    with app.app_context():
        book = Models.BookModel.get(1)
        print(book)


if __name__ == "__main__":
    main()