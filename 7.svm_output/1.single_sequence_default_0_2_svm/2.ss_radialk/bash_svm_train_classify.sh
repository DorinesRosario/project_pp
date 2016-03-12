#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/4.SingleSeq_sets/7.svm_singleseq_radial/
svm_path=/home/rosario/Desktop/svm_light/


for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_learn -t 2 $i.train $i.model 
done

for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_classify $i $i.model $i.pred
done