#!/bin/bash
input_dir_svm_files=/home/rosario/Desktop/project_pp/6.new_svm/2.psi-blast_svm/1.psi_blast_sets/

for file_i in $input_dir_svm_files/*.svm; do
	for file_j in $input_dir_svm_files/*.svm; do
		if [ $file_i != $file_j ]; then
			cat $file_j >> $file_i.train
		fi
	done
done

