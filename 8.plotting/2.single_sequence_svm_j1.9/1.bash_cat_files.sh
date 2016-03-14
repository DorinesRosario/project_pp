#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j1.9/
output_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j1.9/

for file in $input_files/*.pred; do

	cat *.pred >> ss_k0_j1.9.pred.all

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt