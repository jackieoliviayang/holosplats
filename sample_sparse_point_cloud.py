import open3d as o3d
import json
import random
import sys

def sample_sparse_point_cloud(input_ply_file, num_points, output_json_file):
    # Load the point cloud
    point_cloud = o3d.io.read_point_cloud(input_ply_file)
    
    # Get the points and colors
    points = point_cloud.points
    colors = point_cloud.colors
    
    # Convert to list format
    point_data = [(points[i][0], points[i][1], points[i][2], int(colors[i][0] * 255), int(colors[i][1] * 255), int(colors[i][2] * 255)) for i in range(len(points))]
    
    # Sample num_points randomly
    sampled_points = random.sample(point_data, min(num_points, len(point_data)))
    
    # Create the output JSON structure
    output_data = [{"x": p[0], "y": p[1], "z": p[2], "r": p[3], "g": p[4], "b": p[5]} for p in sampled_points]
    
    # Write to JSON file
    with open(output_json_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=4)
    
    print(f'Successfully wrote {len(output_data)} points to {output_json_file}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python sample_sparse_point_cloud.py <input_ply_file> <num_points> <output_json_file>")
        sys.exit(1)

    input_ply_file = sys.argv[1]
    num_points = int(sys.argv[2])
    output_json_file = sys.argv[3]

    sample_sparse_point_cloud(input_ply_file, num_points, output_json_file)

