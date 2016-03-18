#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/set_by_set/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/pb_K1_J2.35/set_by_set/

for file in $input_files/*.svm1.pred; do
	base=`basename $file .svm1.pred`
	python mcc_script.py $input_files/$base.features.txt $input_files/$base.svm1.pred $output_files/$base.mcc.txt

done

#paste -d '' structure.topology.txt sequence.treated.txt > output.txt