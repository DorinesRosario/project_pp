#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/

for file in $input_files/*.svm1.pred ; do
	base=`basename $file .svm1.pred`
	cat *.svm1.pred >> all.svm.K1.predictions

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt