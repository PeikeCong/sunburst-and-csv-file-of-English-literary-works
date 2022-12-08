import pandas as pd
import plotly.express as px
import plotly

#read data in csv and draw sunburst pie

df = pd.read_csv(r"bb.csv")

#a certain time
#df = df[df['time'].isin([i for i in range(1790,1799 + 1)])]

fig = px.sunburst(
    data_frame=df,
    # Root, branches, leaves, leaves
    path=['genre','subgenre','name', 'work'],  
    color_discrete_sequence=px.colors.qualitative.Pastel,
    maxdepth=-2,
)

fig.update_traces(textinfo='label+percent entry')
#fig.update_layout(margin=dict(t=1, l=1, r=1, b=1), uniformtext_minsize=10, uniformtext_mode='hide')

plotly.offline.plot(fig, filename="time.html")


