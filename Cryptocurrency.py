import streamlit as st
import pandas as pd
import time
import plotly.express as px
import mysql_database
import matplotlib.pyplot as plt
import api


df = pd.read_csv('./historical_data.csv')

st.set_page_config(
    page_title='Real-Time Data Science Dashboard',
    page_icon='✅'

)

st.title ("Real-Time Cryptocurrency Price Dashboard")

# name_filter = st.sidebar.selectbox("Select the Name", pd.unique(df['Name']))
# placeholder = st.empty()
# df = df [df['Name']==name_filter]

file = st.file_uploader("Upload your csv file", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())


if file:
   name = df["Name"].unique()
   selected_name = st.sidebar.selectbox("Filter by CryptoCurrencyName",name)
   filtered_data = df[df["Name"] == selected_name]
   st.dataframe(filtered_data)



