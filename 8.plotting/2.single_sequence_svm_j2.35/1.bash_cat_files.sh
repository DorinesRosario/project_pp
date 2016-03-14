#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j2.35/
output_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_j2.35/

for file in $input_files/*.pred; do

	cat *.pred >> ss_k0_j2.35.pred.all

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt