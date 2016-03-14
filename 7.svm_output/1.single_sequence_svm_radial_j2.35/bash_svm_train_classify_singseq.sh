#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.new_svm/1.single_sequence_svm_radial_j2.35/
svm_path=/home/rosario/Desktop/svm_light/

for k in 2 ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $k -j 2.35 $i.train "${i}${k}".model &>"${i}${k}${j}".learn.log
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${k}".model "${i}${k}".pred &>"${i}${k}${j}".classify.log
	done
done