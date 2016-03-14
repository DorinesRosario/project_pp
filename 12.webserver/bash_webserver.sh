#!/bin/bash

"""
#introduce a protein sequence for study:

introduce_seq_script = /home/rosario/Desktop/project_pp/12.webserver/step1_intro_seq/
output_intro_seq = /home/rosario/Desktop/project_pp/12.webserver/step2_seq_in_study/

python ws_step1_input_seq.py $output_intro_seq

"""

#perfom psi-blast in input sequence:

input_sequence = /home/rosario/Desktop/project_pp/12.webserver/step2_seq_in_study/
output_psi_blast = /home/rosario/Desktop/project_pp/12.webserver/step3_psi-blast_output/

for sequence in $input_sequence/*.txt ; do
	base=`basename $sequence .txt`
	blastpgp -j 3 -d /home/rosario/Desktop/uniref90files/uniref90.fasta -i ${sequence} -o $output_dir/$base.blastpgp -Q $output_dir/$base.psi

done 