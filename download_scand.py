import os
import time
from pyDataverse.api import NativeApi, DataAccessApi
from pyDataverse.models import Dataverse
import requests

base_url = 'https://dataverse.tdl.org/'

# Try without authentication first (public dataset)
api = NativeApi(base_url)
data_api = DataAccessApi(base_url)

DOI = "doi:10.18738/T8/0PRYRH"

try:
    dataset = api.get_dataset(DOI)
except Exception as e:
    print(f"Error fetching dataset: {e}")
    print("This dataset may require authentication. Please generate your own API token.")
    exit(1)

if not os.path.exists("random_mdps"):
    os.makedirs("random_mdps")
if not os.path.exists("delivery_mdp"):
    os.makedirs("delivery_mdp")

# Read the list of bag files to download from txt file
txt_file = "scand_bags.txt"  # Change this to your txt file name
if not os.path.exists(txt_file):
    print(f"Error: {txt_file} not found!")
    exit(1)

with open(txt_file, 'r') as f:
    # Read lines and clean them (remove whitespace, bullets, asterisks, etc.)
    desired_files = []
    for line in f:
        # Strip whitespace and remove common bullet characters
        cleaned = line.strip().lstrip('*').lstrip('-').lstrip('•').strip()
        if cleaned and cleaned.endswith('.bag'):
            desired_files.append(cleaned)

print(f"Looking for {len(desired_files)} bag files from {txt_file}:")
for filename in desired_files:
    print(f"  - {filename}")
print()

files_list = dataset.json()['data']['latestVersion']['files']

# Function to download a file with retry mechanism and exponential backoff
def download_file(download_url, dir, filename):
    max_retries = 5
    backoff_factor = 1
    for attempt in range(max_retries):
        try:
            with requests.get(download_url, stream=True) as response:
                response.raise_for_status()
                with open(os.path.join(dir, filename), "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"✓ Successfully downloaded: {filename}")
            return True
        except requests.RequestException as e:
            wait_time = backoff_factor * (2 ** attempt)
            print(f"Error downloading {filename}: {str(e)}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    print(f"✗ Failed to download {filename} after {max_retries} attempts.")
    return False

# Download files
downloaded_count = 0
not_found_files = desired_files.copy()

for file in files_list:
    filename = file["dataFile"]["filename"]
    
    # Check if this file is in our desired list
    if filename in desired_files:
        file_id = file["dataFile"]["id"]
        print(f"Downloading: {filename} (id: {file_id})")
        
        # Construct the download URL
        download_url = f"{base_url}api/access/datafile/{file_id}"
        
        # Determine the directory
        dir = "delivery_mdp/" if "DELIVERY" in filename else "random_mdps/"
        
        # Download the file
        if download_file(download_url, dir, filename):
            downloaded_count += 1
            not_found_files.remove(filename)

print(f"\n{'='*60}")
print(f"Download process completed.")
print(f"Successfully downloaded: {downloaded_count}/{len(desired_files)} files")

if not_found_files:
    print(f"\n⚠ Warning: {len(not_found_files)} files not found in dataset:")
    for filename in not_found_files:
        print(f"  - {filename}")
