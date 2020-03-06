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
    a_assault_searh_for_list = ['AGGRAVATED ASSAULT', 'BRANDISH', 'ARSON']
    drugs_search_for_list = ['DRUG', 'NARCOTICS', 'DRUGS', 'NARCOTICS']
    violations_search_for_list = ['KIDNAPPING','EXTORTION','TRESPASSING', 'VANDALISM', 'VIOLATION', 'PAROLE', 'MUNICIPAL CODE', 'CONTEMPT OF COURT']
    sex_search_for_list = ['LEWD', 'INDECENT EXPOSURE', 'SEX']
    rape_search_for_list = ['RAPE']
    weapon_search_for_list = ['DISCHARGE FIREARMS/SHOTS FIRED']
    
    if 'Date Occurred' in df.columns:
        df['date'] = pd.to_datetime(df['Date Occurred'])
        df['victim_female'] = [1 if x == 'F' else 0 for x in df['Victim Sex']]
        df['victim_hispanic'] = [1 if x == 'H' else 0 for x in df['Victim Descent']]
        df['victim_white'] = [1 if x == 'W' else 0 for x in df['Victim Descent']]
        df['victim_black'] = [1 if x == 'B' else 0 for x in df['Victim Descent']]
        df['victim_asian'] = [1 if x == 'C' else 0 for x in df['Victim Descent']]
        
        df['crime_description_recoded'] = df['Crime Code Description']
        
        df['larceny'] = df['Crime Code Description'].str.contains('|'.join(theft_search_for_list))
        df.loc[df.larceny, 'crime_description_recoded'] = 'Larceny'
        
        df['car_theft'] = df['Crime Code Description'].str.contains('|'.join(car_theft_search_for_list))
        df.loc[df.car_theft, 'crime_description_recoded'] = 'Vehicle Theft'
        
        df['robbery'] = df['Crime Code Description'].str.contains('|'.join(robbery_search_for_list))
        df.loc[df.robbery, 'crime_description_recoded'] = 'Robbery'
        
        df['burglary'] = df['Crime Code Description'].str.contains('|'.join(burglary_search_for_list ))
        df.loc[df.burglary, 'crime_description_recoded'] = 'Burglary'
        
        df['other_assault'] = df['Crime Code Description'].str.contains('|'.join(o_assault_search_for_list))
        df.loc[df.other_assault, 'crime_description_recoded'] = 'Other Assaults'
        
        df['aggravated_assault'] = df['Crime Code Description'].str.contains('|'.join(a_assault_searh_for_list))
        df.loc[df.aggravated_assault, 'crime_description_recoded'] = 'Aggravated Assault'
        
        df['drugs'] = df['Crime Code Description'].str.contains('|'.join(drugs_search_for_list))
        df.loc[df.drugs, 'crime_description_recoded'] = 'Narcotic Drug Laws'
        
        df['violation'] = df['Crime Code Description'].str.contains('|'.join(violations_search_for_list))
        df.loc[df.violation, 'crime_description_recoded'] = 'Miscellaneous Other Violations'
        
        df['sex'] = df['Crime Code Description'].str.contains('|'.join(sex_search_for_list))
        df.loc[df.sex, 'crime_description_recoded'] = 'Sex (except rape/prst)'
        
        df['rape'] = df['Crime Code Description'].str.contains('|'.join(rape_search_for_list))
        df.loc[df.rape, 'crime_description_recoded'] = 'Rape'
        
        df['weapon'] = df['Crime Code Description'].str.contains('|'.join(weapon_search_for_list))
        df.loc[df.weapon, 'crime_description_recoded'] = 'Weapon'
        
    elif 'Arrest Date' in df.columns:
        df['date'] = pd.to_datetime(df['Arrest Date'])
        df = df.dropna(subset=['Charge Description'])
    else:
        print("Did not find 'Date Occurred' or 'Arrest Date' in variables")
        return df
    
    df['week'] = df['date'].dt.strftime('%Y-w%U')
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday_name
    
    df = pd.concat([df,pd.get_dummies(df['weekday'])], axis=1)
    df = pd.concat([df,pd.get_dummies(df['month'], prefix = 'month')], axis=1)
    df = pd.concat([df,pd.get_dummies(df['Area Name'])], axis=1)
    
    df = df.drop(['Unnamed: 0'], axis=1)
    
    return df