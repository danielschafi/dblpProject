from Models import SearchOrderModel
from app import app, db
from maindash import dashApp
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
import requests

import pandas as pd

url = "http://localhost:5000"
engine_url = 'postgresql://postgres:1234@localhost/dblp'

headers = {"Content-Type": "application/json"}

def getOrderDropdown():
    engine = create_engine(engine_url)

    Session = sessionmaker(engine)

    with Session() as  session:
        availableOrders = session.execute(
            select(SearchOrderModel).filter_by(current_status=SearchOrderModel.STATUS_FINISHED)
        ).scalars().all()
        
    return [{"label": f"Id: {order.id}, Keyword: {order.keyword}, Start: {order.start_node}", "value": order.id } for order in availableOrders], availableOrders[-1].id
    
    
def getOrders():
    engine = create_engine(engine_url)

    Session = sessionmaker(engine)

    with Session() as  session:
        orders = session.execute(
            select(SearchOrderModel).filter_by(current_status=SearchOrderModel.STATUS_FINISHED)
        ).scalars().all()
        
    # create new dataframe with data and return datafram witha all orders
    return pd.DataFrame([vars(o) for o in orders])
    
    
def postNewOrder(startNode, keyword,):
    order = {
        "start_node" : startNode,
        "keyword" : keyword,
        
        
    }
    
    response = requests.post(url=url+"/searchorders/1", data=order, headers=headers)
    return response.status_code