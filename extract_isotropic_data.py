import struct
import json
import math

def read_ply_file(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = []
        while True:
            line = f.readline().decode().strip()
            header.append(line)
            if line == 'end_header':
                break

        # Parse header
        header_info = {}
        for line in header:
            if line.startswith('element'):
                parts = line.split()
                if parts[1] == 'vertex':
                    header_info['vertex_count'] = int(parts[2])
            elif line.startswith('property'):
                parts = line.split()
                property_name = parts[2]
                header_info.setdefault('properties', []).append(property_name)

        vertex_count = header_info['vertex_count']
        properties = header_info['properties']

        # Indices for the required properties
        pos_indices = [properties.index('x'), properties.index('y'), properties.index('z')]
        scale_indices = [properties.index('scale_0'), properties.index('scale_1'), properties.index('scale_2')]
        rot_indices = [properties.index('rot_0'), properties.index('rot_1'), properties.index('rot_2'), properties.index('rot_3')]
        opacity_index = properties.index('opacity')

        # Read vertex data
        extracted_data = []
        for _ in range(vertex_count):
            # Read each vertex data
            vertex_data = f.read(struct.calcsize('f' * len(properties)))
            unpacked_data = struct.unpack('f' * len(properties), vertex_data)

            # Extract required properties
            position = [unpacked_data[i] for i in pos_indices]
            scale = [unpacked_data[i] for i in scale_indices]
            rotation = [unpacked_data[i] for i in rot_indices]
            opacity = unpacked_data[opacity_index]

            # Process scales 
            scale = [math.exp(s) for s in scale]
            opacity = 1 / (1 + math.exp(-opacity))

            extracted_data.append({
                'position': position,
                'scale': scale,
                'rotation': rotation,
                'opacity': opacity
            })

    return extracted_data

def main():
    ply_file = 'outputs/nerfstudio_data/splatfacto/2024-10-18_180358/splat.ply'  # Updated file path
    output_file = 'extracted_isotropic_data.json'  # Name of the output JSON file
    data = read_ply_file(ply_file)

    # Write extracted properties to JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data has been written to {output_file}")

if __name__ == "__main__":
    main()

