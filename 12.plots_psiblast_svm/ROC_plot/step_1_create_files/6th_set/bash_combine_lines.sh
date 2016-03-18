#!/bin/sh

input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/ROC_plot/step_1_create_files/6th_set/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/ROC_plot/step_1_create_files/6th_set/

for file in $input_files/*.predictions; do
	base=`basename $file .predictions`
	paste -d ' ' $input_files/psi_blast_set6.features $input_files/$base.predictions > $output_files/$base.roc_step1.txt

done