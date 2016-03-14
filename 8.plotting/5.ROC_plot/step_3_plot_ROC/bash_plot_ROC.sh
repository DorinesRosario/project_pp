#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/8.plotting/5.ROC_plot/step_2_sort_files/
output_files=/home/rosario/Desktop/project_pp/8.plotting/5.ROC_plot/step_2_sort_files/

for file in $input_files/*.txt; do
	base=`basename $file .txt`
	python ROC_sort_step2.py $input_files/$base.txt $output_files/$base.sorted.txt

done