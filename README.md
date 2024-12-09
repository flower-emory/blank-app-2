import streamlit as st
import pandas as pd
import numpy as np
all_users = ["Allie","Emory","Elsie","Feliciry","uncle z","Dad","Kate the great","ant Flo","mom","Lottie"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")
np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()
# tab1, tab2 = st.tabs(["Chart", "Dataframe"])
# tab1.line_chart(data, height=250)
st.data_editor(data, height=250, use_container_width=True)