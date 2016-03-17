#!/bin/bash



#Step 1
#introduce a protein sequence for study:
#_______________________________________


python ws_step1_input_seq.py $output_intro_seq


#Step 2
#perfom psi-blast in input sequence:
#___________________________________


input_sequence=/home/rosario/Desktop/project_pp/12.webserver/sequence.fasta
uniref_pathway=/home/rosario/Desktop/uniref90files/uniref90.fasta
blastpgp -a 3 -j 3 -d $uniref_pathway -i $input_sequence -o $input_sequence.blastpgp -Q $input_sequence.psi &>input_sequence.log





#Step 3
#parse the psi-blast output into svm format: 
#___________________________________________

	#step1: parse aa probs info
	#__________________________

input_files=/home/rosario/Desktop/project_pp/12.webserver/
output_files=/home/rosario/Desktop/project_pp/12.webserver/

for file in $input_files/*.psi; do
	base=`basename $file .psi`
	python ws_step3_parse_psiblast_aa.py $input_files/$base.psi $output_files/$base.aa_parsed.txt

done


	#step2: parse conservation info
	#______________________________

input_files=/home/rosario/Desktop/project_pp/12.webserver/
output_files=/home/rosario/Desktop/project_pp/12.webserver/

for file in $input_files/*.psi; do
	base=`basename $file .psi`
	python ws_step3_parse_psiblast_conservation.py $input_files/$base.psi $output_files/$base.conservation_parsed.txt

done


	#step3: combine lines from parsed files --> psi_blast svm format
 	#_______________________________________________________________


input_files=/home/rosario/Desktop/project_pp/12.webserver/
output_files=/home/rosario/Desktop/project_pp/12.webserver/

for file in $input_files/*.aa_parsed.txt; do
	base=`basename $file .aa_parsed.txt`
	paste -d '' $input_files/$base.aa_parsed.txt $input_files/$base.conservation_parsed.txt > $output_files/$base.svm 

done


	#step4: introduce '0' in the begining of every line to be possible to classify
	#_____________________________________________________________________________


input_files=/home/rosario/Desktop/project_pp/12.webserver/
output_files=/home/rosario/Desktop/project_pp/12.webserver/

for file in $input_files/*.svm; do
	base=`basename $file .svm`
	python ws_step3_parse_psiblast_add0.py $input_files/$base.svm $output_files/$base.final.svm

done





#Step 4
#run svm *classification* in psi_blast parsed file from sequence of interest using best svm model from my predictor
#__________________________________________________________________________________________________________________

input_dir_svm_files=/home/rosario/Desktop/project_pp/12.webserver/sequence.fasta.final.svm
pred_pathway=/home/rosario/Desktop/project_pp/12.webserver/predictor.model
svm_path=/home/rosario/Desktop/svm_light/


$svm_path/svm_classify $input_dir_svm_files $pred_pathway output.svm.pred





#Step 5
#return a prediction to the input sequence
#_________________________________________


input_files=/home/rosario/Desktop/project_pp/12.webserver/
output_files=/home/rosario/Desktop/project_pp/12.webserver/

for file in $input_files/*.pred; do
	base=`basename $file .pred`
	python ws_step5_beta_prediction.py $input_files/$base.pred $output_files/$base.prediction.txt

done

