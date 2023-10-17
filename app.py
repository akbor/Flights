import streamlit as st
import requests
import pandas as pd

url = r"https://www.sydneyairport.com.au/_a/flights?flightType=arrival&terminalType=domestic&filter=&date=2023-10-17&count=10&startFrom=0&seq=2&sortColumn=scheduled_time&ascending=true&showAll=false"

response = requests.get(url)

if response.ok:
    # st.write(response.json())
    
    tbl = pd.read_json(response.json())
    