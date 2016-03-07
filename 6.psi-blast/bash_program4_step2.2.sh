#!/bin/bash
structure_input_files=/home/rosario/Desktop/project_pp/6.psi-blast/seq_structures/
topology_output_files=/home/rosario/Desktop/project_pp/6.psi-blast/seq_topology/

for file in $structure_input_files/*.txt; do
	base=`basename $file .txt`
	python program4_step2.2_topology.py $file $topology_output_files/$base.topology.txt

done
