#!/usr/bin/env python2
import numpy as np
import math
import neighborcount as nc
import setting.py
setting.init();
canei=nc.neigh(setting.period);
caall=np.loadtxt(setting.cafile);
balist=set(range(period*period*period))-set(caall);
balist=list(balist);
noca=set(caall)-set(canei);
noca=sorted(list(noca))
sin=[];
dou=[];
ba_ca=[];
count=np.zeros((7,1));
for i in balist:
	temp=nc.searchAone(i,period);
	common=set(caall)-(set(caall)-set(temp));
	ba_ca.append([len(common),i]);# the first variable store how many ca neighbors you have for this site, the second stores the atom_tick
	count[len(common)]=count[len(common)]+1;
data=np.loadtxt("final.txt");
sum=np.zeros((7,3));# this actually predicts the number of ca neighbor atoms and it's influence.
for i in ba_ca:
    sum[i[0]]=np.add(sum[i[0]],data[i[1]]);
for i in range(7):
	sum[i]=np.divide(sum[i],count[i]);
print sum
