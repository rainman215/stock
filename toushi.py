#!/usr/bin/python
#coding=gbk
import os
import pandas as pd
file='./data/pe.xlsx'
pd.pivot_table(file,values=['name'],columns=['pe'])