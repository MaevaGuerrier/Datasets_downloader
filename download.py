#!/usr/bin/env python3
"""
Download helper for tartan and scand datasets.
Uses HTTP requests to download files from URLs.
"""

import os
import requests
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from pathlib import Path
import time

def download_file(url, destination):
    """
    Download a file from a URL to a destination path with progress bar.
    
    Args:
        url (str): URL to download from
        destination (str): Path where the file should be saved
    """
    os.makedirs(os.path.dirname(destination) or '.', exist_ok=True)
    
    response = requests.get(url, stream=True, timeout=30)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(destination, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=os.path.basename(destination)) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
    
    print(f"Downloaded: {destination}")


def download_hurron_dataset(output_dir="datasets/huron"):
    """
    Download the Huron dataset.
    
    Args:
        output_dir (str): Directory where the dataset should be saved
    
    Returns:
        bool: True if download was successful, False if URLs are not configured or download fails
    """
    def _get_folders(url):
        """Extract all folder names from the index page"""
        print(f"Fetching main directory listing from {url}...")
        response = requests.get(url, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        folders = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('/') and href not in ['../', '../', '/datasets/']:
                folder_name = href.rstrip('/')
                folders.append(folder_name)
        
        return folders

    def _get_bag_files(folder_url):
        """Get all .bag files from a folder"""
        response = requests.get(folder_url, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        bag_files = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.bag'):
                bag_files.append(href)
        
        return bag_files

    print("Downloading Huron dataset...")
    # If in future they change or add mor indexes add them here
    huron_index_url = "https://rail.eecs.berkeley.edu/datasets/huron/"

    if not huron_index_url:
        print("Warning: No URLs configured for Huron dataset. Please add URLs to download.py")
        return False
    
    try:

        folders = _get_folders(huron_index_url)

        for folder in folders:
            folder_url = urljoin(huron_index_url, folder + '/')
            bag_files = _get_bag_files(folder_url)

            if len(bag_files) == 0:
                print(f" No .bag files found, skipping {folder_url}\n")
                continue

            for bag_file in bag_files:
                url = urljoin(folder_url, bag_file)
                filename = os.path.join(output_dir, folder, bag_file)
                download_file(url, filename)

        print("Huron dataset download complete!")
        return True
    except Exception as e:
        print(f"Error downloading Huron dataset: {e}")
        return False




if __name__ == "__main__":
    print("This is a helper module. Use datasets_downloader.py to download datasets.")
