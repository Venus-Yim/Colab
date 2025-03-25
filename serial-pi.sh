#!/usr/bin/env bash
#SBATCH -J serial-pi
#SBATCH -p compute
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=3G

# Load the computing environment we need
module load python3

# Execute the task
python pi.py 100000000
