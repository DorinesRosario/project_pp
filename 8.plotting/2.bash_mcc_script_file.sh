#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/3.psi-blast1st_default_k2/
output_files=/home/rosario/Desktop/project_pp/8.plotting/3.psi-blast1st_default_k2/

for file in $input_files/*.txt; do
	base=`basename $file .txt`
	python mcc_script.py $input_files/$base.txt $input_files/$base.svm.prediction $output_files/$base.mcc_all.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt