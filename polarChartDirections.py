import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'},    {'type': 'polar'}]])

r = [1,2,3,4,5]
theta = [0,90,180,360,0]

fig.add_trace(go.Scatterpolar(), 1, 1)

# Same data for the two Scatterpolar plots, we will only change the direction in the layout
fig.update_traces(r= r, theta=theta,
                  mode="lines+markers", line_color='indianred',
                  marker=dict(color='lightslategray', size=8, symbol='square'))
fig.update_layout(
    showlegend = False,
    polar = dict(
      radialaxis_tickfont_size = 8,
      angularaxis = dict(
        tickfont_size=8,
        rotation=90, # start position of angular axis
        direction="counterclockwise"
      )
    ),
    polar2 = dict(
      radialaxis_tickfont_size = 8,
      angularaxis = dict(
        tickfont_size = 8,
        rotation = 90,
        direction = "clockwise"
      ),
    ))

fig.show()