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
import position as ps
import setting
setting.init();
f=open(setting.traject_file,"r");
cell=setting.period;
raw_data=f.readlines();
lines=len(raw_data);
step=lines/(5*cell*cell*cell+9);
atomlist=range(0,cell*cell*cell);
traject=[];
posit=[];
varall=[];
for atomnum in atomlist:
    traject=[];
    neilist=ps.neighbor_o_forA(atomnum,cell);
    for i in range(step):
        atomposit=ps.getposition(atomnum,cell,i,raw_data);
        posit.append(atomposit);
        sum=np.zeros(3);
        for j in range(12):
            pi=ps.getposition(neilist[j],cell,i,raw_data);
            p=ps.getperiodical(cell,i,raw_data);
            dis=ps.disp(atomposit,pi,p);
            sum=sum+dis;
        sum=sum/12.0;
        traject.append(list(sum));
    varall.append(np.var(traject,axis=0));
final=open("final.txt","w");
for j in varall:
    final.write(str(j[0])+" "+str(j[1])+" "+str(j[2])+"\n");
