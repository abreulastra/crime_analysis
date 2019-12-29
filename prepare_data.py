#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:51:15 2019

This program's goal is to data from the LA police deparment about crime and
police arrests, and keep the last year of data available.
The original files include ten years of data, which introduces two issues for
the analysis: a )Inconsistencies between the early and more recent years, and 
the size of the files (+700 MB)

Note: the original files will not be included in the github repository, only 
the output of this code.

The source this data comes from:
https://www.kaggle.com/cityofLA/los-angeles-crime-arrest-data
    
@author: abreulastra
"""

import pandas as pd
from datetime import timedelta



path = 'los-angeles-crime-arrest-data/'
cri = pd.read_csv(path + 'crime-data-from-2010-to-present.csv')
arr = pd.read_csv(path + 'arrest-data-from-2010-to-present.csv')

cri['Date Occurred'] = pd.to_datetime(cri['Date Occurred'])
#cri.sort_values(cri['Date Occurred'], inplace = True)
latest_cri = cri['Date Occurred'].max()
cutt_off_cri = latest_cri + timedelta(days=-180)
cri = cri[cri['Date Occurred'] > cutt_off_cri]

arr['Arrest Date'] = pd.to_datetime(arr['Arrest Date'])
#arr.sort_values(arr['Arrest Date'], inplace = True)
latest_arr = arr['Arrest Date'].max()
cutt_off_arr = latest_arr + timedelta(days=-180)
arr = arr[arr['Arrest Date'] > cutt_off_arr]

cri.to_csv(path + 'crime-data.csv')
arr.to_csv(path + 'arrest-data.csv')