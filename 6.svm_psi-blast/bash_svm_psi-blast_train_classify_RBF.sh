#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/4.SingleSeq_sets/4.svm_sinseq_files/
svm_path=/home/rosario/Desktop/svm_light/


for c in 2.8 3.5 4 ; do
	for g in `seq -0.5 0.5 0.7` ; do
	
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t 2 -c $c -g $w $i.train "${i}${c}${g}".model 
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${c}${g}".model "${i}${c}${g}".pred

done