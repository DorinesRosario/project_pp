#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/helices_singseq/
output_files=/home/rosario/Desktop/project_pp/helices_singseq/

for file in $input_files/*.svm.predictions; do
	base=`basename $file .svm.predictions`
	python mcc_script.py $input_files/$base.svm.helices $input_files/$base.svm.predictions $output_files/$base.all.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt