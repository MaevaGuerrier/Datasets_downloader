#!/usr/bin/env python3
"""
Download helper for tartan and scand datasets.
Uses HTTP requests to download files from URLs.
"""

import os
import requests
from tqdm import tqdm


def download_file(url, destination):
    """
    Download a file from a URL to a destination path with progress bar.
    
    Args:
        url (str): URL to download from
        destination (str): Path where the file should be saved
    """
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(destination, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=os.path.basename(destination)) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
    
    print(f"Downloaded: {destination}")


def download_tartan_dataset(output_dir="datasets/tartan"):
    """
    Download the Tartan dataset.
    
    Args:
        output_dir (str): Directory where the dataset should be saved
    """
    print("Downloading Tartan dataset...")
    # Placeholder URLs - replace with actual Tartan dataset URLs
    tartan_urls = [
        # Add actual Tartan dataset URLs here
        # Example: "https://example.com/tartan/data.zip"
    ]
    
    if not tartan_urls:
        print("Warning: No URLs configured for Tartan dataset. Please add URLs to download.py")
        return
    
    for url in tartan_urls:
        filename = os.path.join(output_dir, os.path.basename(url))
        download_file(url, filename)
    
    print("Tartan dataset download complete!")


def download_scand_dataset(output_dir="datasets/scand"):
    """
    Download the Scand dataset.
    
    Args:
        output_dir (str): Directory where the dataset should be saved
    """
    print("Downloading Scand dataset...")
    # Placeholder URLs - replace with actual Scand dataset URLs
    scand_urls = [
        # Add actual Scand dataset URLs here
        # Example: "https://example.com/scand/data.zip"
    ]
    
    if not scand_urls:
        print("Warning: No URLs configured for Scand dataset. Please add URLs to download.py")
        return
    
    for url in scand_urls:
        filename = os.path.join(output_dir, os.path.basename(url))
        download_file(url, filename)
    
    print("Scand dataset download complete!")


if __name__ == "__main__":
    print("This is a helper module. Use datasets_downloader.py to download datasets.")
