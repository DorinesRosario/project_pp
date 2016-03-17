#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/1.only_features_sets/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/1.only_features_sets/

for file in $input_files/*.svm; do
	base=`basename $file .svm`
	python sets_features.py $input_files/$base.svm $output_files/$base.features.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt