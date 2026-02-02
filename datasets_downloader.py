#!/usr/bin/env python3
"""
Datasets Downloader
Download various vision datasets: recon, tartan, scand, go_stanford, huron, or all.
"""

import argparse
import os
import sys
import gdown
from download import download_tartan_dataset, download_scand_dataset


# Google Drive file IDs for datasets that use gdown
DATASET_GDRIVE_IDS = {
    "recon": None,  # Add actual Google Drive file ID
    "go_stanford": None,  # Add actual Google Drive file ID
    "huron": None,  # Add actual Google Drive file ID
}


def download_with_gdown(dataset_name, file_id, output_dir):
    """
    Download a dataset from Google Drive using gdown.
    
    Args:
        dataset_name (str): Name of the dataset
        file_id (str): Google Drive file ID
        output_dir (str): Directory where the dataset should be saved
    """
    if file_id is None:
        print(f"Warning: No Google Drive file ID configured for {dataset_name} dataset.")
        print(f"Please update DATASET_GDRIVE_IDS in datasets_downloader.py")
        return False
    
    print(f"Downloading {dataset_name} dataset from Google Drive...")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{dataset_name}.zip")
    url = f"https://drive.google.com/uc?id={file_id}"
    
    try:
        gdown.download(url, output_path, quiet=False)
        print(f"{dataset_name} dataset downloaded successfully to {output_path}")
        return True
    except Exception as e:
        print(f"Error downloading {dataset_name}: {e}")
        return False


def download_recon(output_dir="datasets/recon"):
    """Download the Recon dataset using gdown."""
    return download_with_gdown("recon", DATASET_GDRIVE_IDS["recon"], output_dir)


def download_go_stanford(output_dir="datasets/go_stanford"):
    """Download the Go Stanford dataset using gdown."""
    return download_with_gdown("go_stanford", DATASET_GDRIVE_IDS["go_stanford"], output_dir)


def download_huron(output_dir="datasets/huron"):
    """Download the Huron dataset using gdown."""
    return download_with_gdown("huron", DATASET_GDRIVE_IDS["huron"], output_dir)


def download_tartan(output_dir="datasets/tartan"):
    """Download the Tartan dataset using download.py helper."""
    return download_tartan_dataset(output_dir)


def download_scand(output_dir="datasets/scand"):
    """Download the Scand dataset using download.py helper."""
    return download_scand_dataset(output_dir)


def process_dataset(dataset_name, dataset_dir):
    """
    Process a dataset for vision-based models.
    This function can be extended to include preprocessing steps like:
    - Image resizing
    - Normalization
    - Data augmentation
    - Creating train/val/test splits
    
    Args:
        dataset_name (str): Name of the dataset
        dataset_dir (str): Directory containing the dataset
    """
    print(f"\nProcessing {dataset_name} dataset for vision-based models...")
    
    if not os.path.exists(dataset_dir):
        print(f"Warning: Dataset directory {dataset_dir} does not exist. Skipping processing.")
        return
    
    # Placeholder for actual processing logic
    # This can be extended based on specific requirements
    print(f"Dataset processing for {dataset_name} would be implemented here.")
    print(f"Typical steps might include:")
    print("  - Extracting compressed files")
    print("  - Organizing images into directories")
    print("  - Creating metadata files")
    print("  - Resizing images to standard sizes")
    print("  - Computing dataset statistics")
    
    # Example: List files in the dataset directory
    try:
        files = os.listdir(dataset_dir)
        print(f"Found {len(files)} items in {dataset_dir}")
    except Exception as e:
        print(f"Error accessing dataset directory: {e}")


def download_dataset(dataset_name, process=False, output_dir="datasets"):
    """
    Download a specific dataset and optionally process it.
    
    Args:
        dataset_name (str): Name of the dataset to download
        process (bool): Whether to process the dataset after downloading
        output_dir (str): Base directory for datasets
    """
    dataset_name = dataset_name.lower()
    
    # Map dataset names to their download functions
    downloaders = {
        "recon": lambda: download_recon(os.path.join(output_dir, "recon")),
        "tartan": lambda: download_tartan(os.path.join(output_dir, "tartan")),
        "scand": lambda: download_scand(os.path.join(output_dir, "scand")),
        "go_stanford": lambda: download_go_stanford(os.path.join(output_dir, "go_stanford")),
        "huron": lambda: download_huron(os.path.join(output_dir, "huron")),
    }
    
    if dataset_name not in downloaders:
        print(f"Error: Unknown dataset '{dataset_name}'")
        print(f"Available datasets: {', '.join(downloaders.keys())}")
        return False
    
    print(f"\n{'='*60}")
    print(f"Starting download for: {dataset_name}")
    print(f"{'='*60}")
    
    success = downloaders[dataset_name]()
    
    if success and process:
        dataset_dir = os.path.join(output_dir, dataset_name)
        process_dataset(dataset_name, dataset_dir)
    
    return success


def download_all_datasets(process=False, output_dir="datasets"):
    """
    Download all available datasets.
    
    Args:
        process (bool): Whether to process datasets after downloading
        output_dir (str): Base directory for datasets
    """
    datasets = ["recon", "tartan", "scand", "go_stanford", "huron"]
    
    print(f"\n{'='*60}")
    print("Downloading ALL datasets")
    print(f"{'='*60}\n")
    
    results = {}
    for dataset in datasets:
        results[dataset] = download_dataset(dataset, process, output_dir)
    
    print(f"\n{'='*60}")
    print("Download Summary")
    print(f"{'='*60}")
    for dataset, success in results.items():
        status = "✓ Success" if success else "✗ Failed"
        print(f"{dataset:15} : {status}")
    print(f"{'='*60}\n")


def main():
    """Main entry point for the datasets downloader."""
    parser = argparse.ArgumentParser(
        description="Download vision datasets: recon, tartan, scand, go_stanford, huron, or all",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s recon              # Download only the recon dataset
  %(prog)s all                # Download all datasets
  %(prog)s tartan --process   # Download and process tartan dataset
  %(prog)s all --process      # Download and process all datasets
        """
    )
    
    parser.add_argument(
        "dataset",
        choices=["recon", "tartan", "scand", "go_stanford", "huron", "all"],
        help="Dataset to download (or 'all' for all datasets)"
    )
    
    parser.add_argument(
        "--process",
        action="store_true",
        help="Process the dataset(s) for vision-based models after downloading"
    )
    
    parser.add_argument(
        "--output-dir",
        default="datasets",
        help="Base output directory for datasets (default: datasets)"
    )
    
    args = parser.parse_args()
    
    # Create base output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Download dataset(s)
    if args.dataset == "all":
        download_all_datasets(process=args.process, output_dir=args.output_dir)
    else:
        success = download_dataset(args.dataset, process=args.process, output_dir=args.output_dir)
        if not success:
            sys.exit(1)
    
    print("\nDone!")


if __name__ == "__main__":
    main()
