#!/bin/bash
#SBATCH -p debug
#SBATCH -N 1
#SBATCH -t 00:30:00
#SBATCH -J plotset5
#SBATCH -D $HOME/acme_slurm/logs/
#SBATCH -o set5_driver.o%j

source activate 2.8
$HOME/acme_slurm/ps5_commands.sh