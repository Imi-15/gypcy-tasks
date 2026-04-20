import pandas as pd
import plotly.express as px

# Load Excel file - place 'cpe202 assignment.xlsx' in the same folder as this script
sd = pd.read_excel('cpe202 assignment.xlsx')
print(sd.head())

# Create pie chart
fig = px.pie(sd, values='Sale', names='Ship Mode', hole=0, width=700, height=700)
fig.update_traces(textinfo='none')

# Display in browser
fig.show()
