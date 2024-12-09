import streamlit as st
from sqlitedict import SqliteDict

st.title("this is your savings")

goal = st.number_input("What is your goal?")
st.write("Your current goal is ", goal)


name = st.text_input("What is your name?")
st.write("Nice too meat you ", name)

all_users = [name]
with st.container(border=True):
    user = st.selectbox("User", all_users)

st.balloons()