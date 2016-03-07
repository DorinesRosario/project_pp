#!/bin/bash
paste -d '' topology_svm.txt blast_1step.txt > output.txt

tail -n +3 file1 > file2 # remove first two lines
cat file1 file2 > file3