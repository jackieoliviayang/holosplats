import json
import numpy as np

def calculate_average_scale(json_file):
    # Load the isotropic Gaussian data from the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Initialize a list to hold the scales
    scales = []

    # Extract the scale from each Gaussian and append to the list
    for gaussian in data:
        scale = gaussian['scale'][0]  # Since the scale is isotropic, take the first value
        scales.append(scale)

    # Calculate the average scale
    average_scale = np.mean(scales)

    # Print the average scale
    print(f"Average scale of the isotropic Gaussians: {average_scale}")

if __name__ == '__main__':
    json_file = 'extracted_isotropic_data.json'  # Change this to your file path if needed
    calculate_average_scale(json_file)

