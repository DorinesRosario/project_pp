#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/set_by_set/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K0_J2.35/set_by_set/

for file in $input_files/*.svm0.pred; do
	base=`basename $file .svm0.pred`
	python mcc_script.py $input_files/$base.features.txt $input_files/$base.svm0.pred $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt