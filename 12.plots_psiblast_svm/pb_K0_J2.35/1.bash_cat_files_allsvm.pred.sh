#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/

for file in $input_files/*.svm0.pred ; do
	base=`basename $file .svm0.pred`
	cat *.svm0.pred >> all.K0

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt