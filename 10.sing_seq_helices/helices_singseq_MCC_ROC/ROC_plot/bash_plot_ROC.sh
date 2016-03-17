#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/
output_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/

for file in $input_files/*.sorted.txt; do
	base=`basename $file .sorted.txt`
	python ROC_sort_step3.py $input_files/$base.sorted.txt $output_files/$base.sorted.txt

done