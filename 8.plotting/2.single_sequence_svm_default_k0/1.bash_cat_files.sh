#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_default_k0/
output_files=/home/rosario/Desktop/project_pp/8.plotting/2.single_sequence_svm_default_k0/

for file in $input_files/*.pred; do

	cat *.pred >> ss_def_k0.pred.all

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt