"""
BreathFirstSearch algorithm that is searching
connection-Table to find shortest paths of nodes.
"""
from Models import SearchOrderModel, ConnectModel
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
            status = insertOrder(order)
            if not status:
                order.changeStatus(SearchOrderModel.STATUS_FAILED)
            else:
                order.changeStatus(SearchOrderModel.STATUS_PROCESSING)

def insertOrder(order):
    nodes = getNodes(order.keyword)
    orderId = order.id
    if not nodes:
        return None
    #remove numberOfNodes
    del nodes["numberOfNodes"]
    connectList = []
    order.changeStatus(SearchOrderModel.STAUTS_INSERTING)
    for table, idList in nodes.items():
        for _id in idList:
            connectList.append(ConnectModel(id=_id,tablename=table, orderid=orderId))
    ConnectModel.multiInsert(connectList)
    return 1

    
    

def getNodes(keyword):
    response = requests.get(f"{URL}/api/keyword/{keyword}")
    if response.status_code != 200:
        return None
    nodes = response.json()
    return nodes


if __name__ == "__main__":
    main()