#!/bin/bash
structure_input_files=/home/rosario/Desktop/project_pp/6.psi-blast/psi-blast_output/
topology_output_files=/home/rosario/Desktop/project_pp/6.psi-blast/psi-blast_treated_output/
for file in $structure_input_files/*.psi; do
	base=`basename $file .psi`
	python program4_step1_transform_psi-blast_output.py $file $topology_output_files/$base.treated.txt

done