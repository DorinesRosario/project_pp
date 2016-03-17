#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/

for file in $input_files/*.features.txt ; do
	base=`basename $file .features.txt`
	cat *.features.txt >> all.features

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt