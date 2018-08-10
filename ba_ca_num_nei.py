#!/usr/bin/env python2
import numpy as np
import math
def wash(pointone,pointtwo,pb):
    dis=pb[1]-pb[0];
    if(pointtwo-pointone>dis/2):
        return pointtwo-dis;
    elif(pointtwo-pointone<-1*dis/2):
        return pointtwo+dis;
    else:
        return pointtwo+0.0;
def index3Dto1D(index,p):
    re=(index[0]+p)%p+p*((index[1]+p)%p)+p**2*((index[2]+p)%p)
    return int(re)
def index1Dto3D(index,p):
    a=np.zeros(3);
    a[0]=np.floor(index/p/p);
    a[1]=np.floor((index-a[0]*p*p)/p);
    a[2]=index-a[0]*p*p-a[1]*p;
    return a;
def searchAone(index,p):
    '''index3D=[nx,ny,nz]'''
    nz=int(math.floor(index/(p**2)));
    ny=int(math.floor((index-nz*p**2)/p));
    nx=int(math.floor(index-nz*p**2-ny*p));
    '''first layer'''
    layone=[];
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if(math.fabs(i)+math.fabs(j)+math.fabs(k)==1):
                    layone.append(int(index3Dto1D([nx+i,ny+j,nz+k],p)));
    return layone;
def searchAtwo(index,p):
    '''second layer'''
    nz=int(math.floor(index/(p**2)));
    ny=int(math.floor((index-nz*p**2)/p));
    nx=int(math.floor(index-nz*p**2-ny*p));
    laytwo=[];
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if(math.fabs(i)+math.fabs(j)+math.fabs(k)==2):
                    laytwo.append(index3Dto1D([nx+i,ny+j,nz+k],p));
    return laytwo;
def searchAthree(index,p):
    '''third layer '''
    nz=int(math.floor(index/(p**2)));
    ny=int(math.floor((index-nz*p**2)/p));
    nx=int(math.floor(index-nz*p**2-ny*p));
    laythree=[];
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            for k in range(-1,2,1):
                if(math.fabs(i)+math.fabs(j)+math.fabs(k)==3):
                    laythree.append(index3Dto1D([nx+i,ny+j,nz+k],p));
    return laythree;
def neigh(p):
    calist=open("cadata.txt","r");
    ca=[];
    for i in calist.readlines():
         ca.append(int(i));
    pair=[];
    for i in ca:
        nei=searchAone(i,p);
        common=set(ca)-(set(ca)-set(nei));
        commonlist=list(common);
        for j in commonlist:
            pair.append(j);
            pair.append(i);
    return sorted(list(set(pair)));
def neitp(i,j,p):
    tempi=index1Dto3D(i,p);
    tempj=index1Dto3D(j,p);
    '''this actually told you which neighbor they are:'''
    for i in range(3):
        if(math.fabs(tempi[i]-tempj[i])==1 or math.fabs(tempi[i]-tempj[i])==period-1):
            return 2-i;
period=20;
canei=neigh(period);
caall=np.loadtxt("cadata.txt");
balist=set(range(period*period*period))-set(caall);
balist=list(balist);
noca=set(caall)-set(canei);
noca=sorted(list(noca))
sin=[];
dou=[];
ba_ca=[];
count=np.zeros((7,1));
for i in balist:
	temp=searchAone(i,period);
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
