from Models import SearchOrderModel, ConnectModel
from app import app, db
from maindash import dashApp
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
import requests

import pandas as pd
from globals import orderStatusList

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
        
        if len(availableOrders) > 0:
            return [{"label": f"Id: {order.id}, Keyword: {order.keyword}, Start: {order.start_node}", "value": order.id } for order in availableOrders], availableOrders[-1].id
        else:
            return [], None
        
        
   
    
def getOrdersDf():
    engine = create_engine(engine_url)

    Session = sessionmaker(engine)

    with Session() as  session:
        orders = session.execute(
            select(SearchOrderModel)
        ).scalars().all()
    df= pd.DataFrame([vars(o) for o in orders])[["id", "keyword", "start_node", "max_distance", "current_status"]]

    df["current_status"] = df["current_status"].apply(lambda x: orderStatusList[x])

    return  df
    
    
def postNewOrder(keyword= " ", start_node= " ", email=" ", max_distance=-1):
    order = {
    "keyword": keyword,
    "start_node": start_node,
    "email":email,
    "max_distance": max_distance
    }
    
    response = requests.post(url=url+"/searchorders/1", data=order, headers=headers)
    return response.status_code


def getAllConnectData(orderid):       
    engine = create_engine(engine_url)

    Session = sessionmaker(engine)

    with Session() as  session:
        connectData = session.execute(
            select(ConnectModel).
            filter_by(orderid=orderid)
        ).scalars().all()
        
    if len(connectData) == 0:
        return None
        
            
    df = pd.DataFrame([vars(o) for o in connectData])
    df['node'] = df['tablename'] + ',' + df['id'].astype(str)
    
    df = df.drop(['_sa_instance_state', 'queued', 'tablename', 'id'], axis=1, errors='ignore')

    print(df.columns)
    print(len(df[df["precedent_node"].isnull() == False]))
    
    return df
    