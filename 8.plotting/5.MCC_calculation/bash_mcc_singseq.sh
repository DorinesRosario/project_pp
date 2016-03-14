#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/5.MCC_calculation/
output_files=/home/rosario/Desktop/project_pp/8.plotting/5.MCC_calculation/

for file in $input_files/*.all; do
	base=`basename $file .all`
	python mcc_script.py $input_files/dataset_features.all $input_files/$base.all $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt