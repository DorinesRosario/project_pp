#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/

for file in $input_files/*.K1.svm.predictions; do
	base=`basename $file .K1.svm.predictions`
	python mcc_script.py $input_files/$base.svm.features $input_files/$base.K1.svm.predictions $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt