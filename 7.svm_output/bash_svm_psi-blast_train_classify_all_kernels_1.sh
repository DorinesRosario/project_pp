#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.svm_psi-blast/psi-blast_svm_sets/
svm_path=/home/rosario/Desktop/svm_light/


for k in `seq 0 4` ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $k $i.train "${i}${k}".model &>"${i}${k}".learn.log
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${k}".model "${i}${k}".pred &>"${i}${k}".classify.log
	done
done