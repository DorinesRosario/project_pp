#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/3.psi-blast1st_default_k2/
output_files=/home/rosario/Desktop/project_pp/8.plotting/3.psi-blast1st_default_k2/

for file in $input_files/*.pred; do

	cat *.pred >> all.svm.prediction

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt