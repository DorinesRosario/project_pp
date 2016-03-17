#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_k2_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_k2_J2.35/

for file in $input_files/*.svm2.pred ; do
	base=`basename $file .svm2.pred`
	cat *.svm2.pred >> all.predictions

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt