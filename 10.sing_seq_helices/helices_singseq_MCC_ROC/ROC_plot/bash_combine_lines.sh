#!/bin/sh

input_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/
output_files=/home/rosario/Desktop/project_pp/helices_singseq/ROC_plot/

for file in $input_files/*.svm.predictions; do
	base=`basename $file .svm.predictions`
	paste -d ' ' $input_files/dataset_helices.txt $input_files/$base.svm.predictions > $output_files/$base.roc_step1.txt

done