#!/bin/sh

input_files=/home/rosario/Desktop/project_pp/8.plotting/5.ROC_plot/step_1_create_files/
output_files=/home/rosario/Desktop/project_pp/8.plotting/5.ROC_plot/step_1_create_files/

for file in $input_files/*.pred.all; do
	base=`basename $file .pred.all`
	paste -d ' ' $input_files/dataset_features.txt $input_files/$base.pred.all > $output_files/$base.roc_step1.txt

done