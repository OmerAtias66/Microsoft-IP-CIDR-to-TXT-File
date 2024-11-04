# Built by Omer Atias
import requests
from bs4 import BeautifulSoup
import re
import os.path

# URL of the updated Microsoft's IPs list
url = 'https://networksdb.io/ip-addresses-of/microsoft-corp'

#GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all text in the soup that matches CIDR notation
    cidr_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}\b'
    cidrs = re.findall(cidr_pattern, soup.get_text())

  # Define the path
    ip_directory_path = os.path.join(os.path.expanduser('~'), 'C:\\Users\\user\\MicrosoftIPTXT', 'Microsfot_Updated_Cidrs.txt')

    # Write the CIDR notations to a text file on the IP Directory
    with open(ip_directory_path, 'w') as f:
        for cidr in set(cidrs):  # Use set to avoid duplicates
            f.write(cidr + '\n')

    print(f'Found {len(set(cidrs))} unique CIDRs and saved to {ip_directory_path}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
