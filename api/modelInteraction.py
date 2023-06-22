import json
from Models import SearchOrderModel, ConnectModel
from app import app, db
from maindash import dashApp
from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import sessionmaker
import requests
import re

import pandas as pd
from globals import orderStatusList

url= "http://127.0.0.1:5000/api"
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

def getDataId(title,art):
    engine = create_engine('postgresql://postgres:1234@localhost/dblp')
    if art != None:
        conn = engine.connect()
        query = text(f"SELECT * FROM {art} WHERE title ILIKE '%' || :title || '%'".format(art))
        query = query.bindparams(title=title)
        result = conn.execute(query)
        #get all rows in datafram
        df = result.fetchall()
        df = pd.DataFrame(df)
        df.columns = result.keys()
        # drop all colomns except title and id
        df = df.drop(df.columns.difference(['title', 'id']), 1)
        return df
    return None
    
def postNewOrder(keyword= " ", start_node= " ", email=" ", max_distance=-1):
    order = {
        "keyword": keyword,
        "start_node": start_node,
        "email":email,
        "max_distance": max_distance
    }

    order = json.dumps(order)
    response = requests.post(url=url+"/searchorder/1", data=order, headers=headers)
    return response.status_code


def getAllConnectData(orderid):       
    engine = create_engine(engine_url)

    Session = sessionmaker(engine)

    with Session() as  session:
        connectData = session.execute(
            select(ConnectModel).
            filter_by(orderid=orderid)
        ).scalars().all()
        
        
        start_node = session.execute(
            select(SearchOrderModel).
            filter_by(id=orderid)
            ).scalar_one()
        
    if len(connectData) == 0:
        return None
    
    start_node = vars(start_node)["start_node"]
    df = pd.DataFrame([vars(o) for o in connectData])
    df['node'] = df['tablename'] + ',' + df['id'].astype(str)
    df.loc[df["node"] == start_node, "precedent_node"] = start_node
    df = df.drop(['_sa_instance_state', 'queued', 'id'], axis=1, errors='ignore')
    
    return df



def getNodeData(node):
    table, id = node.split(",")
    
    response = requests.get(f"{url}/{table}/{int(id)}", headers=headers)
    if response.status_code != 200:
        return None
    txt = str(response.content)
    return re.sub(r",","<br>", re.sub(r"{|}|\\n","", txt))


getNodeData("book,390")