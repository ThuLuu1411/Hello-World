#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:21:15 2022

@author: vophuoctri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import matplotlib.dates as mdates
import matplotlib
import os

nhap=False
while nhap==False:
    try:
        """Dan duong link du lieu"""
        link = input("Nhap duong link du lieu: ")
        os.chdir(link)
        
        """Nhap file du lieu"""
        dx = input("Nhap file du lieu su thay doi cua search term: ")
        dx = pd.read_csv(dx)
        print(dx)
        
        df = input("Nhap file du lieu profit: ")
        df = pd.read_csv(df)
        print(df)
        
        """Nhap du lieu gia chung khoan"""
        dy = input("Nhap file du lieu chua gia chung khoan: ")
        dy = pd.read_csv(dy)
        y = dy[["date", "Line"]]
        y.columns = ["date", "VNIndex"]
        print(y)
        
        """Nhap file list tu khoa"""
        l = df.columns[1:].tolist()
        print(l)        
        nhap= True
    except:
        nhap=False

def data(x):
    dl = pd.merge(x,y, on=["date"])
    dl["date"] = pd.DatetimeIndex(dl["date"])
    return dl

def plot(term):
    x1 = data(dx)[["date", "VNIndex"]]
    x2 = data(dx)[["date", term]].set_index("date").transpose()
    fig, ax1 = plt.subplots(figsize=(10,4))
    sns.heatmap(x2, ax=ax1, cmap="vlag", cbar_kws={"location":"left", "pad":0.01}, yticklabels=[])
    ax1.set_ylabel(str("Relative search volumes change: "+str(term)), labelpad=50)
    ax2= ax1.twinx()
    sns.lineplot(x1.index, x1["VNIndex"], ax=ax2)
    return plt.show()

def bar(data):
    dl = data[data.columns[1:]].sum()
    dl = dl.sort_values().reset_index()
    dl.columns = ["kw", "value"]
    fig, ax1 = plt.subplots(figsize=(4,12))
    sns.barplot(x = "value", y="kw", data=dl, ax=ax1)
    return plt.show()