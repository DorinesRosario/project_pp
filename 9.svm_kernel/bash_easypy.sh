#!/bin/bash
input_dir_files=/home/rosario/Desktop/project_pp/9.svm_kernel/


for file in input_dir_files/*.svm; do
	base=`basename $file .txt`
	python easy.py $file.train $file


done