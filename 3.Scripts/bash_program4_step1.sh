#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/5.psi-blast/psi-blast_output/
output_files=/home/rosario/Desktop/project_pp/5.psi-blast/psi-blast_treated_output/
for file in $input_files/*.psi; do
	base=`basename $file .psi`
	python program4_step1_transform_psi-blast_output.py $file $output_files/$base.treated.txt

done