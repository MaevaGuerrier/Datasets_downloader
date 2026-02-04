#!/bin/bash

./init_submodule.sh
mkdir -p datasets
mkdir -p datasets/tartan_drive
cd third_party/tartan_drive/
python3 download_files.py --download-dir datasets/tartan_drive
cd ../..
python3 datasets_downloader.py huron # huron datasets
mkdir -p datasets/go_stanford
cd datasets/go_stanford/
gdown https://drive.google.com/uc\?id=1BVGA46WbvOZFyuzkzV2n_yZqcQsdIJy7
if [ -f go_stanford.zip ]; then
    unzip go_stanford.zip -d .
    echo "go_stanford dataset unzipped."
fi

cd ../..
mkdir -p datasets/recon
cd datasets/recon/
gdown https://rail.eecs.berkeley.edu/datasets/recon-navigation/recon_dataset.tar.gz 
if [ -f recon_dataset.tar.gz ]; then
    tar -xzf recon_dataset.tar.gz
    echo "recon dataset extracted."
fi

cd ../..