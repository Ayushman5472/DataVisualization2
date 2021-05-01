import pandas as pd
import csv
import plotly.graph_objects as pgo

df = pd.read_csv("data1.csv")

Level1 = df.loc[df['level']=="Level 1"]

TRL_987 = df.loc[df['student_id']=="TRL_987"]

Mean = df.groupby('level')["attempt"].mean()
print(Mean)

diagram = pgo.Figure(pgo.Bar(x = Mean, y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation= 'h'))
diagram.show()