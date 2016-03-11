#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step3/
output_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step4/

for file in $input_files/*.svm.txt; do
	base=`basename $file .svm.txt`
	python psi-blast_svm_conservation.py $input_files/$base.svm.txt $input_files/$base.txt $output_files/$base.svm

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt