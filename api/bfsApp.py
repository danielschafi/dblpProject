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

        #get with processing status
        processingOrders = SearchOrderModel.getByStatus(SearchOrderModel.STATUS_SETUP)
        for order in processingOrders:
            processOrder(order)

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
    #if starting_node is already inserted, queue it
    startNodeTableName, startNodeId = order.start_node.split(",")
    startNode = ConnectModel.get(id=startNodeId, orderid=order.id, tablename=startNodeTableName)
    if not startNode:
        #insert stating_node
        startNode = ConnectModel(id=startNodeId, orderid=order.id, tablename=startNodeTableName)
        startNode.save()
    #queue startnode.
    startNode.setVisited()
    startNode.setDistance(0)
    startNode.queue()
    return 1

def getNodes(keyword):
    response = requests.get(f"{URL}/api/keyword/{keyword}")
    if response.status_code != 200:
        return None
    nodes = response.json()
    return nodes

def processOrder(order):
    pass


if __name__ == "__main__":
    main()