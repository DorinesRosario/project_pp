#!/bin/sh

input_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/ROC_plot/step_1_create_files/
output_files=/home/rosario/Desktop/project_pp/12.plots_psiblast_svm/ROC_plot/step_1_create_files/

for file in $input_files/*.pred; do
	base=`basename $file .pred`
	paste -d ' ' $input_files/all.features $input_files/$base.pred > $output_files/$base.roc_step1.txt

done