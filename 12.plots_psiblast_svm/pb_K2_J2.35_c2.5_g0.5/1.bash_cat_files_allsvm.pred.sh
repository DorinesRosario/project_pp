#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K2_J2.35_c2.5_g0.5/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K2_J2.35_c2.5_g0.5/

for file in $input_files/*.svm2.50.5.pred ; do
	base=`basename $file .svm2.50.5.pred`
	cat *.svm2.50.5.pred >> all.K2505.predictions

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt