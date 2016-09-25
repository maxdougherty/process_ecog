#!/bin/bash -l
#SBATCH -p debug
#SBATCH -N 4
#SBATCH -t 00:30:00
#SBATCH -J preprocess_data
#SBATCH -o preprocess_output.o%j

module load python
module unload
module load h5py

export PYTHONPATH="/global/homes/j/jlivezey/ecog:$PYTHONPATH"

srun -N 1 -n 1 -c 32 /global/homes/j/jlivezey/ecog/scripts/subject_scripts/preprocess_ec2.sh &
srun -N 1 -n 1 -c 32 /global/homes/j/jlivezey/ecog/scripts/subject_scripts/preprocess_ec9.sh &
srun -N 1 -n 1 -c 32 /global/homes/j/jlivezey/ecog/scripts/subject_scripts/preprocess_gp31.sh &
srun -N 1 -n 1 -c 32 /global/homes/j/jlivezey/ecog/scripts/subject_scripts/preprocess_gp33.sh &
wait