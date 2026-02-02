# Datasets Downloader

A command-line tool for downloading and processing various vision datasets.

## Supported Datasets

- **recon** - Downloaded using gdown from Google Drive
- **tartan** - Downloaded using the download.py helper
- **scand** - Downloaded using the download.py helper
- **go_stanford** - Downloaded using gdown from Google Drive
- **huron** - Downloaded using gdown from Google Drive
- **all** - Download all datasets at once

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MaevaGuerrier/Datasets_downloader.git
cd Datasets_downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Download a specific dataset:
```bash
python datasets_downloader.py <dataset_name>
```

Available dataset names: `recon`, `tartan`, `scand`, `go_stanford`, `huron`, or `all`

### Examples

Download the recon dataset:
```bash
python datasets_downloader.py recon
```

Download all datasets:
```bash
python datasets_downloader.py all
```

Download and process a dataset for vision-based models:
```bash
python datasets_downloader.py tartan --process
```

Specify a custom output directory:
```bash
python datasets_downloader.py scand --output-dir /path/to/datasets
```

### Command-line Options

- `dataset` - (Required) The dataset to download: `recon`, `tartan`, `scand`, `go_stanford`, `huron`, or `all`
- `--process` - Process the dataset(s) for vision-based models after downloading
- `--output-dir` - Base output directory for datasets (default: `datasets`)

### Help

To see all available options:
```bash
python datasets_downloader.py --help
```

## Dataset Configuration

### For gdown-based datasets (recon, go_stanford, huron)

Edit the `DATASET_GDRIVE_IDS` dictionary in `datasets_downloader.py` to add Google Drive file IDs:

```python
DATASET_GDRIVE_IDS = {
    "recon": "YOUR_GOOGLE_DRIVE_FILE_ID",
    "go_stanford": "YOUR_GOOGLE_DRIVE_FILE_ID",
    "huron": "YOUR_GOOGLE_DRIVE_FILE_ID",
}
```

### For URL-based datasets (tartan, scand)

Edit the URL lists in `download.py` to add direct download URLs:

```python
def download_tartan_dataset(output_dir="datasets/tartan"):
    tartan_urls = [
        "https://example.com/tartan/file1.zip",
        "https://example.com/tartan/file2.zip",
    ]
    # ...
```

## Dataset Processing

The `--process` flag enables post-download processing for vision-based models. This feature can be extended to include:

- Extracting compressed files
- Organizing images into directories
- Creating metadata files
- Resizing images to standard sizes
- Computing dataset statistics
- Creating train/val/test splits
- Data augmentation

Modify the `process_dataset()` function in `datasets_downloader.py` to implement custom processing logic.

## Project Structure

```
Datasets_downloader/
├── datasets_downloader.py  # Main CLI tool
├── download.py             # Helper for URL-based downloads
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── datasets/              # Default output directory (created on first run)
    ├── recon/
    ├── tartan/
    ├── scand/
    ├── go_stanford/
    └── huron/
```

## Dependencies

- `gdown>=4.7.1` - For downloading from Google Drive
- `requests>=2.31.0` - For HTTP downloads
- `tqdm>=4.66.0` - For progress bars

## License

See LICENSE file for details.