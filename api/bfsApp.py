"""
BreathFirstSearch algorithm that is searching
connection-Table to find shortest paths of nodes.
"""
from Models import SearchOrderModel
from app import app 
from db import db
import requests

URL = "http://localhost:5000"

def main():
    db.init_app(app)
    with app.app_context():
        #get open status
        setupOrders = SearchOrderModel.getByStatus(SearchOrderModel.STATUS_SETUP)
        for order in setupOrders:
            insertOrder(order)

def insertOrder(order):
    getNodes(order.keyword)

def getNodes(keyword):
    request = requests.get(f"{URL}/api/relation")
    print(keyword)


if __name__ == "__main__":
    main()