#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K3_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K3_J2.35/

for file in $input_files/*.svm3.pred ; do
	base=`basename $file .svm3.pred`
	cat *.svm3.pred >> all.K3.predictions

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt