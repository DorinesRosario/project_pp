#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.new_svm/1.single_sequence_svm0.27/
svm_path=/home/rosario/Desktop/svm_light/

for k in 0 ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $k -j 0.27 $i.train "${i}${k}".model &>"${i}${k}${j}".learn.log
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${k}".model "${i}${k}".pred &>"${i}${k}${j}".classify.log
	done
done