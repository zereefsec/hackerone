import json
import argparse

def parse_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Filter out empty primary keys
    bounty_data = {key: [item for item in value if item['attributes'].get('eligible_for_bounty')] for key, value in data.items() if any(item['attributes'].get('eligible_for_bounty') for item in value)}

    with open(output_file, 'w') as file:
        json.dump(bounty_data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Process JSON file and export eligible bounties")
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file')

    args = parser.parse_args()

    parse_json(args.input_file, args.output_file)

if __name__ == '__main__':
    main()

