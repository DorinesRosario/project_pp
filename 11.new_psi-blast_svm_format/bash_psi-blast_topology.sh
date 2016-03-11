#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step1/
output_files=/home/rosario/Desktop/project_pp/11.new_psi-blast_svm_format/psi-blast_svm_step3/
for file in $input_files/*.svm; do
	base=`basename $file .svm`
	python psi-blast_svm_topology.py $input_files/$base.topology.txt $input_files/$base.svm $output_files/$base.svm.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt