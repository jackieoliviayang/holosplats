import json
import numpy as np
import plotly.graph_objs as go
import argparse

def plot_sampled_points_to_html(json_file, output_html):
    # Load the sampled points from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract coordinates and RGB values
    points = np.array([[point['x'], point['y'], point['z']] for point in data])
    colors = np.array([[point['r'], point['g'], point['b']] for point in data]) / 255  # Normalize RGB values to [0, 1]

    # Create a 3D scatter plot using Plotly
    trace = go.Scatter3d(
        x=points[:, 0],
        y=points[:, 1],
        z=points[:, 2],
        mode='markers',
        marker=dict(
            size=5,
            color=colors,  # Set color using RGB
            opacity=0.8
        )
    )
    
    layout = go.Layout(
        scene=dict(
            xaxis_title='X Coordinate',
            yaxis_title='Y Coordinate',
            zaxis_title='Z Coordinate'
        ),
        title='Sampled Points with RGB Colors'
    )

    fig = go.Figure(data=[trace], layout=layout)

    # Save the plot as an HTML file
    fig.write_html(output_html)

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Plot sampled points from a JSON file and save to HTML.')
    parser.add_argument('json_file', type=str, help='Input JSON file containing sampled points.')
    parser.add_argument('output_html', type=str, help='Output HTML file for the plot.')
    
    args = parser.parse_args()

    # Call the plotting function with the provided arguments
    plot_sampled_points_to_html(args.json_file, args.output_html)

if __name__ == '__main__':
    main()

