#!/bin/bash
input_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/
output_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/

for file in $input_files/*.roc_step1.txt; do
	base=`basename $file .roc_step1.txt`
	python ROC_sort_step2.py $input_files/$base.roc_step1.txt $output_files/$base.sorted.txt

done