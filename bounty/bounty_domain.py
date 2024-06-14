import json
import sys
import re

def extract_links_urls_domains(json_file, output_file, txt_file, asset_types):
    # Domain patterns to exclude - Need gf tool patterns from tomnomnom to implement this beautifully
    excluded_patterns = [r'play\.google\.com', r'chrome\.google\.com', r'chromewebstore\.google\.com', r'developers\.google\.com', r'docs\.google\.com', r'drive\.google\.com', r'www\.google\.com', r'apps\.apple\.com', r'com\.', r'\.png$', r'\.exe$', 'login.php', 'xmlrpc.php']

    def is_excluded(domain):
        for pattern in excluded_patterns:
            if re.search(pattern, domain):
                return True
        return False

    with open(json_file, 'r') as f:
        data = json.load(f)

    extracted_data = {}
    all_domains = set()  # To store all unique domains

    for key, items in data.items():
        extracted_data[key] = []
        for item in items:
            attributes = item.get("attributes", {})
            current_asset_type = attributes.get("asset_type", "")
            # Filter assets based on user-provided asset_types
            if current_asset_type.lower() in asset_types:
                asset_identifier = attributes.get("asset_identifier", "")
                instruction = attributes.get("instruction", "")
                
                # Extract domains using regex
                urls_domains = re.findall(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b', str(asset_identifier))
                urls_domains += re.findall(r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b', str(instruction))
                
                for link in urls_domains:
                    # Exclude specified domains and filenames
                    if not is_excluded(link):
                        extracted_data[key].append(link)
                        all_domains.add(link)

        # Remove empty primary keys
        if not extracted_data[key]:
            del extracted_data[key]

    # Write JSON output
    with open(output_file, 'w') as f:
        json.dump(extracted_data, f, indent=2)

    # Write domains to text file
    with open(txt_file, 'w') as f:
        for domain in sorted(all_domains):  # Sorting for easier reading
            f.write(domain + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python domain.py input.json output.json output.txt asset_type1 asset_type2 ...")
    else:
        json_file = sys.argv[1]
        output_file = sys.argv[2]
        txt_file = sys.argv[3]
        asset_types = [arg.lower() for arg in sys.argv[4:]]
        extract_links_urls_domains(json_file, output_file, txt_file, asset_types)
