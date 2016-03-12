#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.new_svm/2.psi-blast_svm/1.psi-blast_svm_default_j2.35/
svm_path=/home/rosario/Desktop/svm_light/


for k in 0 2 3 4 ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $k -j 2.35 $i.train "${i}${k}".model &>"${i}${k}".learn.log
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${k}".model "${i}${k}".pred &>"${i}${k}".classify.log
	done
done