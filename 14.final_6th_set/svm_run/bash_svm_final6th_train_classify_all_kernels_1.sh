#!/bin/bash
svm_path=/home/rosario/Desktop/svm_light/


$svm_path/svm_learn -t 2 -j 2.35 /home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_all5.train /home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_all5.model &>/home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_all5.learn.log


$svm_path/svm_classify /home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_set6.svm /home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_all5.model /home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_set6.pred &>/home/rosario/Desktop/project_pp/14.final_6th_set/psi_blast_set6.classify.log

