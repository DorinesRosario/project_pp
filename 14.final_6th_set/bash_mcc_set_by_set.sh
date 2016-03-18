#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/14.final_6th_set/
output_files=/home/rosario/Desktop/project_pp/14.final_6th_set/

for file in $input_files/*.pred; do
	base=`basename $file .pred`
	python mcc_script.py $input_files/$base.features $input_files/$base.pred $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt