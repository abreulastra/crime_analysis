#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:51:06 2019

@author: AbreuLastra_Work
"""
import pandas as pd

def prepare_data(df):
    """
    Input: a pandas data frame either from the crimes or arrest data records
    Output: a pandas data frame + date variables formated as timestamps,
    year-week, and day of week, respectively
    """
    
    car_theft_search_for_list = ['VEHICLE - STOLEN']
    theft_search_for_list = ['THEFT', 'LARCENY', 'STOLEN']
    
    robbery_search_for_list = ['ROBBERY']
    burglary_search_for_list = ['burglary', 'BURGLARY']
    o_assault_search_for_list = ['BATTERY', 'ASSAULT','CRIMINAL THREATS']
    a_assault_searh_for_list = ['AGGRAVATED ASSAULT']
    drugs_search_for_list = ['DRUG', 'NARCOTICS', 'DRUGS', 'NARCOTICS']
    violations_search_for_list = ['TRESPASSING', 'VANDALISM', 'VIOLATION', 'PAROLE', 'MUNICIPAL CODE']
    
    
    if 'Date Occurred' in df.columns:
        df['date'] = pd.to_datetime(df['Date Occurred'])
        df['date_reported'] = pd.to_datetime(df['Date Reported'])
        df['week_reported'] = df['date_reported'].dt.strftime('%Y-w%U')
        df['weekday_reported'] = df['date_reported'].dt.weekday_name
        
        df['crime_description_recoded'] = df['Crime Code Description']
        
        df['car_theft'] = df['Crime Code Description'].str.contains('|'.join(car_theft_search_for_list))
        df.loc[df.car_theft, 'crime_description_recoded'] = 'Vehicle Theft'
        
        df['larceny'] = df['Crime Code Description'].str.contains('|'.join(theft_search_for_list))
        df.loc[df.larceny, 'crime_description_recoded'] = 'Larceny'
        
        df['robbery'] = df['Crime Code Description'].str.contains('|'.join(robbery_search_for_list))
        df.loc[df.robbery, 'crime_description_recoded'] = 'Robbery'
        
        df['burglary'] = df['Crime Code Description'].str.contains('|'.join(burglary_search_for_list ))
        df.loc[df.burglary, 'crime_description_recoded'] = 'Burglary'
        
        df['other_assault'] = df['Crime Code Description'].str.contains('|'.join(o_assault_search_for_list))
        df.loc[df.other_assault, 'crime_description_recoded'] = 'Other Assaults'
        
        df['aggravated_assault'] = df['Crime Code Description'].str.contains('|'.join(a_assault_searh_for_list))
        df.loc[df.aggravated_assault, 'crime_description_recoded'] = 'Aggravated Assault'
        
        df['drugs'] = df['Crime Code Description'].str.contains('|'.join(drugs_search_for_list))
        df.loc[df.drugs, 'Crime Code Description'] = 'Narcotic Drug Laws'
        
        df['violation'] = df['Crime Code Description'].str.contains('|'.join(violations_search_for_list))
        df.loc[df.violation, 'Crime Code Description'] = 'Miscellaneous Other Violations'
        
    elif 'Arrest Date' in df.columns:
        df['date'] = pd.to_datetime(df['Arrest Date'])
    else:
        print("Did not find 'Date Occurred' or 'Arrest Date' in variables")
        return df
    
    df['week'] = df['date'].dt.strftime('%Y-w%U')
    df['weekday'] = df['date'].dt.weekday_name
    return df