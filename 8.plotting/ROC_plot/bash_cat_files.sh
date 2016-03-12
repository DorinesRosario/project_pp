#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/ROC_plot/
output_files=/home/rosario/Desktop/project_pp/8.plotting/ROC_plot/

for file in $input_files/*.svm.pred; do

	cat *.svm.pred >> all.svm.pred

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt