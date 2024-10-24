import json
import plotly.graph_objs as go
import plotly.io as pio

# Input and output file paths
input_file = 'isotropic_pc.json'
output_file = 'isotropic_pc_plot.html'

# Load the point cloud data (positions)
with open(input_file, 'r') as f:
    point_cloud = json.load(f)

# Extract x, y, z coordinates from the positions
x = [point['position'][0] for point in point_cloud]
y = [point['position'][1] for point in point_cloud]
z = [point['position'][2] for point in point_cloud]

# Create a 3D scatter plot using Plotly
trace = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=2,         # Set marker size
        opacity=0.8,    # Marker opacity
        color='blue'    # Color of the points
    )
)

# Define the layout for the plot
layout = go.Layout(
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    ),
    title='Point Cloud Plot',
)

# Create the figure
fig = go.Figure(data=[trace], layout=layout)

# Save the plot as an HTML file
pio.write_html(fig, file=output_file, auto_open=False)

print(f"3D point cloud plot saved as {output_file}")

