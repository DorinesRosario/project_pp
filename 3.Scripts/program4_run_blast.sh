#!/bin/bash
output_dir=/home/rosario/Desktop/STRIDE_predicter/PSI-BLAST/psi_blast_output
psi_blast_input=/home/rosario/Desktop/STRIDE_predicter/PSI-BLAST/psi_blast_input

for file in $psi_blast_input/*.fasta; do 
base=`basename $file .fasta`
blastpgp -j 3 -d /home/rosario/Desktop/uniref90files/uniref90.fasta -i ${file} -o $output_dir/$base.blastpgp -Q $output_dir/$base.psi
done
