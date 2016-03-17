#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_k2_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_k2_J2.35/

for file in $input_files/*.predictions; do
	base=`basename $file .predictions`
	python mcc_script.py $input_files/$base.features $input_files/$base.predictions $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt