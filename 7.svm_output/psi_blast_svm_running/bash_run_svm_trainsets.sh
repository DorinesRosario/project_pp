#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.svm_psi-blast/psi_blast_svm_running/

for file_i in $input_dir_svm_files/*.svm; do
	for file_j in $input_dir_svm_files/*.svm; do
		if [ $file_i != $file_j ]; then
			cat $file_j >> $file_i.train
		fi
	done
done

