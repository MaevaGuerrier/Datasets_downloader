# Datasets Downloader

A command-line tool for downloading and processing various vision datasets.

## Supported Datasets

- **huron** - Downloaded using gdown from Google Drive
- **all** - Download all datasets at once

## Installation

1. Create pyenv

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

TODO 

## Dataset Processing TODO

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


## License

See LICENSE file for details.