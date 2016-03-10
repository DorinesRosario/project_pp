#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/5.psi-blast/psi-blast_svm_format/input/
output_files=/home/rosario/Desktop/project_pp/5.psi-blast/psi-blast_svm_format/output/

for file in $input_files/*.treated.txt; do
	base=`basename $file .treated.txt`
	python program4_step3_psi-blast_svm.py $input_files/$base.topology.txt $input_files/$base.treated.txt $output_files/$base.svm_format.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt