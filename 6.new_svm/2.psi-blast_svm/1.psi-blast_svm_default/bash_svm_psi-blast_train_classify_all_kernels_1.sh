#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.svm_psi-blast/psi_blast_svm_running/
svm_path=/home/rosario/Desktop/svm_light/


for k in 0 2 3 1 4 ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $k -j 3.6 $i.train "${i}${k}".model &>"${i}${k}".learn.log
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${k}".model "${i}${k}".pred &>"${i}${k}".classify.log
	done
done