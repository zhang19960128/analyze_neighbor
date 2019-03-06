#!/usr/bin/env python2
import numpy as np
import math
import neighborcount as nc
import setting
setting.init();
canei=nc.neigh(setting.period);
caall=np.loadtxt(setting.cafile);
period=setting.period;
balist=set(range(period*period*period))-set(caall);
balist=list(balist);
noca=set(caall)-set(canei);
noca=sorted(list(noca))
f_no=open("noneighbor.txt","w");
f_nei_pair=open("neighbor.txt","w");
sin=[];
dou=[];
ca_ca=[];
count=np.zeros((7,1));
for i in caall:
	temp=nc.searchAone(i,period);
	common=set(caall)-(set(caall)-set(temp));
	ca_ca.append([len(common),i]);
	count[len(common)]=count[len(common)]+1;
for i in noca:
    f_no.write(str(int(i))+"\n");
    sin.append(int(i));
for i in canei:
    temp=nc.searchAone(i,period);
    common=set(caall)-(set(caall)-set(temp));
    common=list(common);
    for j in common:
        if(i<j):
            f_nei_pair.write(str(int(i))+" "+str(int(j))+" "+str(nc.neitp(i,j,period))+"\n");
	    dou.append([int(i),int(j),nc.neitp(i,j,period)]);
data=np.loadtxt("final.txt");
sum=np.zeros((7,3));# this actually predicts the number of ca neighbor atoms and it's influence.
for i in ca_ca:
	sum[i[0]]=np.add(sum[i[0]],data[i[1]]);
for i in range(7):
	sum[i]=np.divide(sum[i],count[i]);
print sum
