#!/bin/sh
#$ -S /bin/bash
#$ -v PATH=/home/data/webcomp/RAMMCAP-ann/bin:/sbin:/usr/sbin:/bin:/usr/bin
#$ -v BLASTMAT=/home/data/webcomp/RAMMCAP-ann/blast/bin/data
#$ -v LD_LIBRARY_PATH=/home/data/webcomp/RAMMCAP-ann/gnuplot-install/lib
#$ -v PERL5LIB=/home/hying/programs/Perl_Lib
#$ -q cdhit_webserver.q
#$ -e /home/data/webcomp/web-session/1456928509/1456928509.err
#$ -o /home/data/webcomp/web-session/1456928509/1456928509.out
cd /home/data/webcomp/web-session/1456928509
faa_stat.pl 1456928509.fas.0
cd-hit -i 1456928509.fas.0 -d 0 -o 1456928509.fas.1 -c 0.9 -n 5  -G 1 -g 1 -b 20 -s 0.0 -aL 0.0 -aS 0.0
faa_stat.pl 1456928509.fas.1
clstr_sort_by.pl no < 1456928509.fas.1.clstr > 1456928509.fas.1.clstr.sorted
clstr_list.pl 1456928509.fas.1.clstr 1456928509.clstr.dump
gnuplot1.pl < 1456928509.fas.1.clstr > 1456928509.fas.1.clstr.1; gnuplot2.pl 1456928509.fas.1.clstr.1 1456928509.fas.1.clstr.1.png
clstr_list_sort.pl 1456928509.clstr.dump 1456928509.clstr_no.dump
clstr_list_sort.pl 1456928509.clstr.dump 1456928509.clstr_len.dump len
clstr_list_sort.pl 1456928509.clstr.dump 1456928509.clstr_des.dump des
FET.pl 1456928509.fas.1.clstr 1456928509.fas.1.clstr.anno 1456928509.fas.1.clstr.anno_len.dump 2>1456928509.fas.1.clstr.anno.err
FET.pl 1456928509.fas.1.clstr.sorted 1456928509.fas.1.clstr.sorted.anno 1456928509.fas.1.clstr.anno_no.dump 2>1456928509.fas.1.clstr.sorted.anno.err
tar -zcf 1456928509.result.tar.gz * --exclude=*.dump --exclude=*.env
echo hello > 1456928509.ok
