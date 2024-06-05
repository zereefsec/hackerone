import json
import sys

def main(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    inscope_data = {}
    for key, items in data.items():
        non_empty_items = [item for item in items if item.get("attributes", {}).get("eligible_for_submission", False)]
        if non_empty_items:
            inscope_data[key] = non_empty_items

    with open('inscope.json', 'w') as f:
        json.dump(inscope_data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.json")
    else:
        json_file = sys.argv[1]
        main(json_file)

