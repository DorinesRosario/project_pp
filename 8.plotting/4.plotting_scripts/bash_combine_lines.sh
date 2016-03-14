#!/bin/sh

input_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step1/
output_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step_try/


for file in $input_files/*.svm; do
	base=`basename $file .svm`
	paste -d '' $input_files/$base.topology.txt $input_files/$base.svm > $output_files/$base.svm.txt

done