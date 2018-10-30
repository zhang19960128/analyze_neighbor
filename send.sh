#!/bin/bash
function getconcent(){
rm concent$1;
touch concent$1;
listone=`seq 10 10 90`
listwo=`seq 120 40 260`
listall=$listone" "$listwo
for i in ${listall[@]}
do
	re=`tail -1 info$i.txt`;
	echo $i" "$re >>concent$1
done
}
path=`pwd`;
declare -a concent=( 0.00 0.10 0.20 0.30 0.40 0.60 0.80 1.00)
for j in ${concent[@]}
do
	cd $path/$j;
	getconcent $j
	cp $path/$j/concent$j $path/
	cd $path
done
