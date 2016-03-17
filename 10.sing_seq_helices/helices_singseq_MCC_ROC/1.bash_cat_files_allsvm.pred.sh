#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/helices_singseq/
output_files=/home/rosario/Desktop/project_pp/helices_singseq/

for file in $input_files/*.svm; do

	cat *.svm >> all.svm.helices

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt