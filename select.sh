#!/bin/bash
for i in `seq 1 1000`
do
    ./setfraction_back.py 0.03;
    nei=`./ca_ca_num_nei.py`;
    echo $nei
    if [ $nei == 0 ]
    then
        break;
    fi
done
