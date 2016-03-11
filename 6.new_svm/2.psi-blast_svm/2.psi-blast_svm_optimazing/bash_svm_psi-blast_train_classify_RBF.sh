#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.svm_psi-blast/psi-blast_svm_radial_opt/
svm_path=/home/rosario/Desktop/svm_light/


for c in 2.5 32.5 ; do
	for g in 0.5 3 ; do
	
		for i in $input_dir_svm_files/*.svm ; do
			$svm_path/svm_learn -t 2 -j 3.6 -c $c -g $g $i.train "${i}${c}${g}".model &>"${i}${c}${g}".learn.log
		done

		for i in $input_dir_svm_files/*.svm ; do
			$svm_path/svm_classify $i "${i}${c}${g}".model "${i}${c}${g}".pred &>"${i}${c}${g}".classify.log
		done
	done
done