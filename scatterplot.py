import pandas as pd
import plotly.express as px

df=pd.read_csv("Copy+of+data+-+data.csv")

fig=px.scatter(df,x="data",y="cases",color="countries", size_max=60)
fig.show()