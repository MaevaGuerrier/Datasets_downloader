#!/usr/bin/env python3
"""
Datasets Downloader
Download various vision datasets: recon, tartan, scand, go_stanford, huron, or all.
"""

import argparse
import os
import sys
from download import download_hurron_dataset


def download_huron(output_dir="datasets/huron"):
    """Download the Huron dataset using download.py helper."""
    return download_hurron_dataset(output_dir)


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


def download_dataset(dataset_name, output_dir="datasets"):
    """
    Download a specific dataset and optionally process it.
    
    Args:
        dataset_name (str): Name of the dataset to download
        output_dir (str): Base directory for datasets
    """
    dataset_name = dataset_name.lower()
    
    # Map dataset names to their download functions
    downloaders = {
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
    
    if success:
        dataset_dir = os.path.join(output_dir, dataset_name)
        process_dataset(dataset_name, dataset_dir)
    
    return success


def download_all_datasets(output_dir="datasets"):
    """
    Download all available datasets.
    
    Args:
        output_dir (str): Base directory for datasets
    """
    datasets = ["huron"]
    
    print(f"\n{'='*60}")
    print("Downloading ALL datasets")
    print(f"{'='*60}\n")
    
    results = {}
    for dataset in datasets:
        results[dataset] = download_dataset(dataset, output_dir)
    
    print(f"\n{'='*60}")
    print("Download Summary")
    print(f"{'='*60}")
    for dataset, success in results.items():
        status = "[OK]" if success else "[FAIL]"
        print(f"{dataset:15} : {status}")
    print(f"{'='*60}\n")


def main():
    """Main entry point for the datasets downloader."""
    parser = argparse.ArgumentParser(
        description="Download vision datasets: huron",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s huron              # Download only the huron dataset
  %(prog)s all                # Download all datasets
  %(prog)s huron --process   # Download and process huron dataset
  %(prog)s all --process      # Download and process all datasets
        """
    )
    
    parser.add_argument(
        "dataset",
        choices=["huron", "all"],
        default="all",
        help="Dataset to download (or 'all' for all datasets)."
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
        download_all_datasets(output_dir=args.output_dir)
    else:
        success = download_dataset(args.dataset, output_dir=args.output_dir)
        if not success:
            sys.exit(1)
    
    print("\nDone!")


if __name__ == "__main__":
    main()
