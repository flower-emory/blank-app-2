import streamlit as st
from sqlitedict import SqliteDict

st.title("this is your savings")

goal = st.number_input("What is your goal?")
st.write("Your current goal is ", goal)


name = st.text_input("What is your name?")
st.write("Nice too meat you ", name)


# If you want to edit a LIST!
name_list = st.data_editor(
    ["$0.00"], 
    num_rows="dynamic"
)

st.text(name_list)

st.balloons()
st.write("you have reached your goal")