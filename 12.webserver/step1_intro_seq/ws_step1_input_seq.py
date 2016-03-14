#WEBSERVER: input a protein sequence:

protein_sequence = raw_input('Introduce a protein sequence:')
print protein_sequence


###### is it better to check first if it is a protein sequence??????


input_sequence = open ('input_sequence.txt', 'w')
for sequence in protein_sequence:
	input_sequence.write(sequence)

input_sequence.close()