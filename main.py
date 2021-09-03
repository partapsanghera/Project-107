import csv
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data.csv")
mean = df.groupby(["Student_ID", "Level"], as_index = False)["Attempt"].mean()
fig = px.scatter(mean, x="Student_ID", y="Level", size="Attempt", color="Attempt")

fig.show()