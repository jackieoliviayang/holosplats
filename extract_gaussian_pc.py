import json

# Input and output file paths
input_file = 'extracted_gaussian_data.json'
output_file = 'gaussian_pc.json'

# Load the extracted_gaussian_data.json file
with open(input_file, 'r') as f:
    data = json.load(f)

# Extract only the positions
positions = [{"position": obj["position"]} for obj in data]

# Save the extracted positions to a new JSON file
with open(output_file, 'w') as f:
    json.dump(positions, f, indent=4)

print(f"Extracted positions have been saved to {output_file}")

