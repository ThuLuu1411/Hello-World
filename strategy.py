# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
import os


nhap = False
while nhap==False:
    try:
        """Dan duong link du lieu"""
        link = input("Nhap duong link du lieu: ")
        os.chdir(link)
        
        """Nhap file du lieu"""
        df = input("Nhap file du lieu: ")
        df = pd.read_csv(df)
        df = df.replace(0, np.nan)
        df = df.dropna(axis=1)
        print(df)
        
        """Nhap du lieu VNIndex"""
        vn = input("Nhap file du lieu VNIndex: ")
        y = pd.read_csv(vn)[["date","Line"]]
        y.columns = ["date","VNIndex"]
        print(df)
        
        
        """Nhap file list tu khoa"""
        l = df.columns[1:].tolist()
        print(l)
        nhap=True
    except: 
        nhap=False
        

class Term:
    def __init__(self, term, dt):
        self.name = df[term]
        self.dt = dt
    def get(self):
        return self.name
    def relative_change(self):
        N = pd.DataFrame()
        for i in range(self.dt):
            N[i]=self.name.shift(i)
        N = N.mean(axis=1)
        dn = self.name - N
        return dn
    def get_strategy(self):
        short = Term.relative_change(self)>0
        strategy = pd.DataFrame()
        strategy["date"] = df["date"]
        strategy["short"] = short
        strategy = pd.merge(strategy, y, on="date")
        return strategy
    def R(self):
        R = []
        for i in range(len(df)):
            if Term.get_strategy(self)["short"][i]==True:
                try:
                    R.append((np.log(Term.get_strategy(self)["VNIndex"][i])-np.log(Term.get_strategy(self)["VNIndex"][i+1])))
                except:
                    break
            else:
                try:
                    R.append((np.log(Term.get_strategy(self)["VNIndex"][i+1])-np.log(Term.get_strategy(self)["VNIndex"][i])))
                except:
                    break
        return R
    
# profit = pd.DataFrame()
# relative_change = pd.DataFrame()

# for i in l:
#     profit[i] = Term(i,4).R()
#     relative_change[i] = Term(i,4).relative_change()
    
# print(profit)
# print(relative_change)

# profit["date"] = df["date"]
# relative_change["date"] = df["date"]
# columns = ["date"] + l
# profit = profit[columns]
# relative_change = relative_change[columns]
# profit.to_csv("profit.csv", index=False)
# relative_change.to_csv("relative_change.csv", index=False)