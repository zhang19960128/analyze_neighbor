#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:49:38 2018
Radial distribution of Ca trajectories
@author: jiahaoz
"""
import numpy as np
import math
import sys
import setting
def changeback(nx,ny,nz,p):
    re=(nx+p)%p+p*((ny+p)%p)+p**2*((nz+p)%p)
    return int(re)
'''compute the vector form v1 to v2 under periodical boundary condition'''
def disp(v1,v2,p):
    vec=np.zeros(3);
    for i in range(3):
        temp=v2[i]-v1[i];
        temp=(temp/p[i]-round(temp/p[i]))*p[i];
        vec[i]=temp;
    return vec;
def changeindex(index,cell):
    index3D=np.zeros(3);
    index3D[2]=int(math.floor(index/cell/cell));
    index3D[1]=int(math.floor((index-index3D[2]*cell*cell)/cell));
    index3D[0]=int(index-index3D[1]*cell-index3D[2]*cell*cell);
    return index3D
def neighbor_o_forA(index,cell):
    index_3D=changeindex(index,cell);
    nei=np.zeros(12);
    nei[0]=changeback(index_3D[0],index_3D[1],index_3D[2],cell);
    nei[1]=changeback(index_3D[0]-1,index_3D[1],index_3D[2],cell);
    nei[2]=changeback(index_3D[0],index_3D[1]-1,index_3D[2],cell);
    nei[3]=changeback(index_3D[0]-1,index_3D[1]-1,index_3D[2],cell);
    nei[4]=changeback(index_3D[0],index_3D[1],index_3D[2],cell)+cell*cell*cell;
    nei[5]=changeback(index_3D[0]-1,index_3D[1],index_3D[2],cell)+cell*cell*cell;
    nei[6]=changeback(index_3D[0]-1,index_3D[1],index_3D[2]-1,cell)+cell*cell*cell;
    nei[7]=changeback(index_3D[0],index_3D[1],index_3D[2]-1,cell)+cell*cell*cell;
    nei[8]=changeback(index_3D[0],index_3D[1],index_3D[2],cell)+2*cell*cell*cell;
    nei[9]=changeback(index_3D[0],index_3D[1]-1,index_3D[2],cell)+2*cell*cell*cell;
    nei[10]=changeback(index_3D[0],index_3D[1],index_3D[2]-1,cell)+2*cell*cell*cell;
    nei[11]=changeback(index_3D[0],index_3D[1]-1,index_3D[2]-1,cell)+2*cell*cell*cell;
    for i in range(12):
        nei[i]=nei[i]+2*cell*cell*cell;
    return nei;
def getposition(iatom,cell,time,raw_data):
    '''time range from 0-the maximum'''
    period=5*cell*cell*cell+9;
    line=raw_data[time*period+int(iatom)+9];
    raw=line.split();
    for i in range(3):
        raw[i]=float(raw[i]);
    return raw
def getperiodical(cell,time,raw_data):
    period=5*(cell**3)+9;
    line1=raw_data[time*period+5];
    line2=raw_data[time*period+6];
    line3=raw_data[time*period+7];
    px=line1.split();
    py=line2.split();
    pz=line3.split();
    for i in range(2):
        px[i]=float(px[i]);
        py[i]=float(py[i]);
        pz[i]=float(pz[i]);
    return [px[1]-px[0],py[1]-py[0],pz[1]-pz[0]];
def cart2sph(cartisian):
    x=cartisian[0];
    y=cartisian[1];
    z=cartisian[2];
    hxy = np.hypot(x, y);
    r = np.hypot(hxy, z);
    theta= np.arctan2(z, hxy)*180/math.pi;
    theta=90-theta;
    phi = np.arctan2(y, x)*180/math.pi;
    if(phi<0):
        phi=phi+360;
    else:
        phi=phi;
    return [r,theta,phi];
def angle(vector_a,vector_b):
    inner=np.dot(vector_a,vector_b);
    a_norm=np.dot(vector_a,vector_a);
    b_norm=np.dot(vector_b,vector_b);
    angle=math.acos(inner/math.sqrt(a_norm)/math.sqrt(b_norm));
    return angle/math.pi*180;
def maxangle(traject):
    le=len(traject);
    angleall=[];
    for i in range(le):
        for j in range(i):
            ag=angle(traject[i],traject[j]);
            print ag
            angleall.append(ag);
    return max(angleall)
if __name__=="__main__":
	setting.init();
	f=open(traject_file,"r");
	cell=period;
	raw_data=f.readlines();
	lines=len(raw_data);
	step=lines/(5*cell*cell*cell+9);
	calist=[int(sys.argv[2])];
	traject=[];
	posit=[];
	for atomnum in calist:
		neilist=neighbor_o_forA(atomnum,cell);
		for i in range(step):
			atomposit=getposition(atomnum,cell,i,raw_data);
			posit.append(atomposit);
			sum=np.zeros(3);
			for j in range(12):
				pi=getposition(neilist[j],cell,i,raw_data);
				p=getperiodical(cell,i,raw_data);
				dis=disp(atomposit,pi,p);
				sum=sum+dis;
				sum=sum/12.0;
				traject.append(sum);
	length=len(traject);
	for j in range(length):
		sph=cart2sph(traject[j]);
		print str(traject[j][0])+" "+str(traject[j][1])+" "+str(traject[j][2])
"""
print maxangle(traject)
"""
