import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Sales Analysis")

# Load Excel file
sd = pd.read_excel('cpe202 assignment.xlsx')
st.write(sd.head())

# Create pie chart
fig = px.pie(sd, values='Sale', names='Ship Mode', hole=0, width=700, height=700, 
             title='Sales by Ship Mode')
fig.update_traces(textinfo='none')

# Display in Streamlit (NOT fig.show())
st.plotly_chart(fig)
