from Models import SearchOrderModel
from app import app, db
from maindash import dashApp
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker


import pandas as pd


URL = "http://localhost:5000"

def getOrderDropdown():
    engine = create_engine('postgresql://postgres:1234@localhost/dblp')

    Session = sessionmaker(engine)

    with Session() as  session:
        availableOrders = session.execute(
            select(SearchOrderModel).filter_by(current_status=SearchOrderModel.STATUS_FINISHED)
        ).scalars().all()
        
    return [{"label": f"Id: {order.id}, Keyword: {order.keyword}, Start: {order.start_node}", "value": order.id } for order in availableOrders], availableOrders[-1].id
    
    
def getOrders():
    engine = create_engine('postgresql://postgres:1234@localhost/dblp')

    Session = sessionmaker(engine)

    with Session() as  session:
        availableOrders = session.execute(
            select(SearchOrderModel).filter_by(current_status=SearchOrderModel.STATUS_FINISHED)
        ).scalars().all()
        
    # create new dataframe with data and return datafram witha all orders
        
    return [{"label": f"Id: {order.id}, Keyword: {order.keyword}, Start: {order.start_node}", "value": order.id } for order in availableOrders], availableOrders[-1].id
    