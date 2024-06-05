import argparse
import json
import requests

def get_scopes(handle):
    scopes = []
    page_number = 1
    while True:
        url = f"https://api.hackerone.com/v1/hackers/programs/{handle}/structured_scopes?page%5Bnumber%5D={page_number}&page%5Bsize%5D=100"
        headers = {
            "Authorization": "Basic emVyZWVmLXNlYzpUN0s1TzZoUjZLQVpKcG9jSjhXQlRXTm1CMUxWT2lXQ1ZjNzdUOWN2Rko0PQ=="
        }  # Replace <your_api_key_here> with your actual API key
        response = requests.get(url, headers=headers)
        data = response.json().get("data", [])
        if not data:
            break
        scopes.extend(data)
        page_number += 1
    return scopes

def main(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    handles = [item['attributes']['handle'] for item in data]
    all_scopes = {}

    for handle in handles:
        scopes = get_scopes(handle)
        all_scopes[handle] = scopes

    with open('scope.json', 'w') as f:
        json.dump(all_scopes, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch structured scopes for handles in a JSON file")
    parser.add_argument("json_file", help="Path to the JSON file containing handles")
    args = parser.parse_args()
    main(args.json_file)

