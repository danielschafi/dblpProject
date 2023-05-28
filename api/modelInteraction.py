
from Models import SearchOrderModel
from app import app
from db import db

URL = "http://localhost:5000"

def getOrderDropdown():
    db.init_app(app)
    with app.app_context():
        availableOrders = SearchOrderModel.getByStatus(SearchOrderModel.STATUS_FINISHED)
        
    orderDict = [{'label': f"Id: {order.id},\tKeyword: {order.keyword},\tStart: {order.start_node}", 'value': order.id } for order in availableOrders]

    print(orderDict)
        
        
        

getOrderDropdown()