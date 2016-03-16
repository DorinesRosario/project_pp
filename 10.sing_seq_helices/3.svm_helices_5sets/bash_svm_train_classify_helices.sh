#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/10.sing_seq_helices/3.svm_helices_5sets/
svm_path=/home/rosario/Desktop/svm_light/


for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_learn $i.train $i.model &>"${i}".learn.log
done

for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_classify $i $i.model $i.pred &>"${i}".classify.log
done