import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("dataset-1.csv")


print(df.groupby("student_id", as_index = False)["attempt"].mean() )
mean = df.groupby("student_id", as_index = False)["attempt"].mean()

fig = px.scatter(mean, x = 'student_id', y = "level", color ="attempt", size = "attempt")
fig.show()

