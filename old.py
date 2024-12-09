import streamlit as st
import pandas as pd
import numpy as np
from sqlitedict import SqliteDict

def save_data(name, data):
    with SqliteDict("example.sqlite", autocommit=True) as db:
        db[name] = data
def get_data(name):
    with SqliteDict("example.sqlite") as db:
        try:
            return db[name]
        except KeyError:
            st.error(f"Data named {name} not found")
            return None
        
name = st.text_input("What's the name of the data?")
save, load = st.tabs(["Save data", "Load data"])

number = st.number_input("Insert a goal")
st.write("The current goal is ", number)


all_users = ["Allie","Emory","Elsie","Felicity","uncle z","Dad","Kate the great","ant Flo","mom"]
with st.container(border=True):
    user = st.selectbox("User", all_users)


with save:
    st.write("Data to save:")
    numbers = st.data_editor([h, 2, 3, 4, 5], num_rows='dynamic')
    if st.button("Save"):
        save_data(name, numbers)
        st.toast(f"Data saved to `{name}`")
with load:
    if st.button("Load"):
        st.toast(f"Loading data `{name}`")
        st.write(get_data(name))




































































































































