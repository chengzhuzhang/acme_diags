#!/bin/bash
#SBATCH -p debug
#SBATCH -N 1
#SBATCH -t 00:30:00
#SBATCH -D $HOME/acme_slurm/logs/
#SBATCH -J plotset5
#SBATCH -o set5_driver.o%j

source activate 2.8
ps5_commands.sh