#!/bin/sh
files="/home/rosario/Desktop/project_pp/6.new_svm/2.psi-blast_svm/1.psi_blast_sets/*.svm"
for i in $files
do
  sed '/^$/d' $i > $i.out
  mv  $i.out $i
done