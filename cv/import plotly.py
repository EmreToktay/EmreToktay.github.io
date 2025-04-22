import plotly.graph_objects as go
import pandas as pd

# Your data
industries = ['Technology', 'BPO', 'Data Management', 'Hospitality', 
              'SaaS', 'Search Engines', 'Hardware', 'Software', 
              'Igaming', 'Fintech']
rankings = [3, 4, 2, 4, 4, 1, 2, 2, 1, 3]

# Create DataFrame
df = pd.DataFrame({
    'Industry': industries,
    'Engagement': rankings,
    'Parent': ['Experience']*len(industries)  # Simplified root node
})

# Create the visualization
fig = go.Figure(go.Treemap(
    labels = ['Experience'] + df['Industry'].tolist(),
    parents = [''] + ['Experience']*len(df),
    values = [0] + df['Engagement'].tolist(),
    marker_colors = ['lightgray'] + ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', 
                                   '#FFA15A', '#19D3F3', '#FF6692', '#B6E880',
                                   '#FF97FF', '#FECB52'],  # Distinct colors
    textinfo = "label+value",
    branchvalues = "total",
    pathbar = {"visible": True}
))

# Update layout
fig.update_layout(
    title = "<b>My Industry Experience</b><br>Size shows engagement level",
    margin = {"t": 60, "l": 0, "r": 0, "b": 0},
    width = 800,
    height = 600
)

# Save as HTML to ensure it works
fig.write_html("industry_experience.html", auto_open=True)

# Also show in notebook if running in Jupyter
fig.show()