import streamlit as st
from sqlitedict import SqliteDict

from sqlitedict import SqliteDict

def save_data(name, data):
    with SqliteDict("example.sqlite", autocommit=True) as db:
        db[name] = data

def get_data(name):
    with SqliteDict("example.sqlite") as db:
        try:
            return db[name]
        except KeyError:
            return None

st.title("this is your savings")

st.write("""
* Write your name
* Write your goal 
* Put in the amount you have saved
* And when you come back just
* Write your name
  """)

name = st.text_input("What is your name?")
st.write("Nice to meet you ", name)

if name not in st.session_state:
    data=get_data(name)
    if not data:
        data=[0.00]
    st.session_state[name] = data

#data = get_data(name)

goal = st.number_input("What is your goal?", value=5)
st.write("Your current goal is ", goal)


money_list = st.data_editor(
    st.session_state[name], 
    num_rows="dynamic",
)
money=0

for coin in money_list:
    money=money+coin
st.write(money)

if goal <= money:
    st.balloons()
    st.write("you have reached your goal")

save_data(name,money_list)