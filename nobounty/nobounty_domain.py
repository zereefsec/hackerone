import json
import sys
import re

def extract_links_urls_domains(json_file, output_json_file, output_txt_file, asset_types):
    # Domain patterns to exclude
    excluded_domains = {
        'hackerone.com', 'github.com', 'play.google.com', 'apps.apple.com', 
        'wearehackerone.com', 'wordpress.org', 'com.*', 'login.php', 'xmlrpc.php'
    }

    with open(json_file, 'r') as f:
        data = json.load(f)

    extracted_data = {}
    all_domains = set()  # To store all unique domains

    for key, items in data.items():
        extracted_data[key] = []
        for item in items:
            attributes = item.get("attributes", {})
            current_asset_type = attributes.get("asset_type", "")
            # Filter assets based on user provided asset_types
            if current_asset_type.lower() in asset_types:
                asset_identifier = attributes.get("asset_identifier", "")
                instruction = attributes.get("instruction", "")
                
                # Extract domains using regex
                urls_domains = re.findall(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b', str(asset_identifier))
                urls_domains += re.findall(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b', str(instruction))
                
                for link in urls_domains:
                    # Exclude specified domains
                    if not re.match(r'com\.', link) and link not in excluded_domains:
                        extracted_data[key].append(link)
                        all_domains.add(link)

        # Remove empty primary keys
        if not extracted_data[key]:
            del extracted_data[key]

    # Write JSON output
    with open(output_json_file, 'w') as f:
        json.dump(extracted_data, f, indent=2)

    # Write domains to text file
    with open(output_txt_file, 'w') as f:
        for domain in sorted(all_domains):  # Sorting for easier reading
            f.write(domain + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python domain.py input.json output.json output.txt asset_type1 asset_type2 ...")
    else:
        json_file = sys.argv[1]
        output_json_file = sys.argv[2]
        output_txt_file = sys.argv[3]
        asset_types = [arg.lower() for arg in sys.argv[4:]]
        extract_links_urls_domains(json_file, output_json_file, output_txt_file, asset_types)
