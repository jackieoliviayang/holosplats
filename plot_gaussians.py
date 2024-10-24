import json
import numpy as np
import plotly.graph_objects as go

def quaternion_to_rotation_matrix(q):
    """Convert a quaternion into a rotation matrix."""
    w, x, y, z = q
    return np.array([
        [1 - 2*y**2 - 2*z**2, 2*x*y - 2*w*z, 2*x*z + 2*w*y],
        [2*x*y + 2*w*z, 1 - 2*x**2 - 2*z**2, 2*y*z - 2*w*x],
        [2*x*z - 2*w*y, 2*y*z + 2*w*x, 1 - 2*x**2 - 2*y**2]
    ])

def load_gaussian_data(filename):
    """Load Gaussian data from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def plot_gaussians(data):
    """Plot Gaussians based on position, scale, rotation, and opacity."""
    fig = go.Figure()

    for gaussian in data:
        position = np.array(gaussian["position"])
        scale = np.array(gaussian["scale"])
        rotation = np.array(gaussian["rotation"])
        opacity = gaussian["opacity"]

        # Convert quaternion to rotation matrix
        rotation_matrix = quaternion_to_rotation_matrix(rotation)

        # Apply rotation to position
        rotated_position = rotation_matrix @ position

        # Create a grid of points representing the Gaussian distribution
        x = np.linspace(rotated_position[0] - scale[0], rotated_position[0] + scale[0], 100)
        y = np.linspace(rotated_position[1] - scale[1], rotated_position[1] + scale[1], 100)
        z = np.linspace(rotated_position[2] - scale[2], rotated_position[2] + scale[2], 100)
        X, Y, Z = np.meshgrid(x, y, z)

        # Calculate the Gaussian function
        gauss = (1 / (np.sqrt(2 * np.pi) * scale[0])) * \
                 np.exp(-0.5 * ((X - rotated_position[0]) ** 2 / scale[0] ** 2 +
                                 (Y - rotated_position[1]) ** 2 / scale[1] ** 2 +
                                 (Z - rotated_position[2]) ** 2 / scale[2] ** 2))

        # Normalize and apply opacity
        gauss = gauss / np.max(gauss) * opacity

        # Add the Gaussian to the plot
        fig.add_trace(go.Scatter3d(
            x=X.flatten(),
            y=Y.flatten(),
            z=Z.flatten(),
            mode='markers',
            marker=dict(size=3, color=gauss.flatten(), opacity=0.5),
            name=f'Gaussian at {rotated_position}'
        ))

    # Update layout
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            title='3D Gaussian Distribution',
        ),
        showlegend=True
    )

    # Save the plot as an HTML file
    fig.write_html('gaussian_plot.html')
    print("Plot saved as 'gaussian_plot.html'.")

if __name__ == "__main__":
    # Load data from JSON file
    json_file = 'extracted_gaussian_data.json'
    gaussian_data = load_gaussian_data(json_file)
    
    # Plot the Gaussians
    plot_gaussians(gaussian_data)

