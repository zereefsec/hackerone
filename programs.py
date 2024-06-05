import requests
import json

def send_request(page_number):
    url = f"https://api.hackerone.com/v1/hackers/programs?page%5Bnumber%5D={page_number}&page%5Bsize%5D=100"
    headers = {
        "Host": "api.hackerone.com",
        "Authorization": "Basic emVyZWVmLXNlYzpUN0s1TzZoUjZLQVpKcG9jSjhXQlRXTm1CMUxWT2lXQ1ZjNzdUOWN2Rko0PQ=="
    }
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    page_number = 1
    all_data = []

    while True:
        response = send_request(page_number)
        if not response.get('data'):
            break
        all_data.extend(response['data'])
        page_number += 1

    with open('programs.json', 'w') as outfile:
        json.dump(all_data, outfile, indent=2)

    print("Data saved to 'programs.json'.")

if __name__ == "__main__":
    main()

