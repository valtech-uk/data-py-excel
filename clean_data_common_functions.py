"""
@author: jondowning
"""

import pandas as pd 

#make everything lower case
df = df.applymap(lambda x: x if type(x)!=str else x.lower())


# Basic exploration
df['col_1'].unique()
df.nunique()
df.describe()



# Ensure data in column is from a 
def string_in_list_validation(x):
    """
    Cleaning of items in column 
    For example 
    if 'option_1' is desired and 'a) option_1' presented then --> 'option_1'
    
    If item is not in list_of_options, return initial input 
    """
    list_of_options = ['option_1', 'option_2']
    
    output = x
    for option in list_of_options:
        if option in x:
            output = option
            
    return output

df['col_1'] = df['col_1'].map(string_in_list_validation)


# Basic / specific cleaning using lambda functions 
df['col_1'] = df['col_1'].map(lambda x: 'goodbye' if x== 'good-bye' else x)



# Setup for SQL queries against dataframes 
import pandasql as pdsql
pysql = lambda q: pdsql.sqldf(q, globals())

example_sql_query = 'SELECT * FROM df WHERE df.col_1 == \"goodbye\"'
df = pysql(example_sql_query)