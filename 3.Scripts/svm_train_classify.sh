#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/4.SingleSeq_sets/4.svm_sinseq_files/
svm_path=/home/rosario/Desktop/svm_light/


for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_learn $i.train $i.model 
done

for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_classify $i $i.model $i.pred
done