import json
import argparse

def parse_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Ensure the keys are processed correctly
    filtered_data = {}
    for key, value in data.items():
        filtered_items = [item for item in value if item['attributes'].get('eligible_for_bounty') is False]
        if filtered_items:  # Check if there are non-empty items
            filtered_data[key] = filtered_items

    with open(output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Process JSON file and export non-eligible bounties")
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file')

    args = parser.parse_args()

    parse_json(args.input_file, args.output_file)

if __name__ == '__main__':
    main()

