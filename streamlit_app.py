import streamlit as st
from sqlitedict import SqliteDict

st.title("this is your savings")

goal = st.number_input("What is your goal?")
st.write("Your current goal is ", goal)


name = st.text_input("What is your name?")
st.write("Nice to meet you ", name)



money_list = st.data_editor(
    [0.00], 
    num_rows="dynamic"
)

st.text(money_list)

money=0

for coin in money_list:
    money=money+coin
st.write(money)

if goal <= money:
    st.balloons()
    st.write("you have reached your goal")