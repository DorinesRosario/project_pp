#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/6.psi-blast/psi-blast_svm_sets/prep_files/
output_files=/home/rosario/Desktop/project_pp/6.psi-blast/psi-blast_svm_sets/prep_set_files/
for file in $input_files/*.txt; do
	base=`basename $file .txt`
	python prep_set_files.py $file $output_files/$base.txt

done