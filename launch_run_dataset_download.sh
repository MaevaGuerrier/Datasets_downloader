#!/bin/bash

#SBATCH --account=def-beltrame
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1000M
#SBATCH --time=00-12:00
#SBATCH --output=%N-%j.out


RUNNAME=${SLURM_ARRAY_JOB_ID}
echo $RUNNAME


module load StdEnv/2023 python/3.10 gcc/12.3


cd /home/maguez/projects/def-beltrame/vnm_datasets/Datasets_downloader
source datadownloader_venv/bin/activate

./download_all_local.sh



