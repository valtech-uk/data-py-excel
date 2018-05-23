"""
@author: jondowning
"""

import pandas as pd 
import numpy as np
import random 
import string


def create_random_data(schema, n):
    # The column headers are the same as the keys in the schema dictionary
    column_headers = list(schema.keys())
    
    # Make the data frame in memory with zeros 
    random_data = pd.DataFrame(0, index=np.arange(n), columns=column_headers)
    
    # Dates list for random date
    dates = pd.date_range('2017-01-01', periods=1000, freq='D')
    
    # Function for generating random string lists 
    def random_string(length):
        return ''.join(random.choice(string.ascii_letters) for m in range(length))
    
    def random_string_list(size, length): 
        return [random_string(length) for x in range(0,size)]
    
    # For each column create random data from the values in the schema dictionary
    for column in column_headers:
        value = schema[column]
        
        if not value: # List is empty
            # Open string 
            random_data[column] = random_string_list(n, 10)
        elif value[0] == 'date':
            # pick random dates from the above 
            random_data[column] = pd.to_datetime(np.concatenate([np.random.choice(dates, size=n, replace=True)]))
        elif value[0] == 'num_range':
            # Random list in range 
            random_data[column] = [random.choice(range(0, 1000)) for x in range(0,n)]
        else: # Take random from option from list 
            random_data[column] = [random.choice(value) for x in range(0,n)]
    
    random_data.sort_index(axis=1, inplace=True)    

    return random_data

if __name__ == '__main__':

    # The schema that describes the dataset 
    schema = {
            'col_1_random': [],
            'col_2_options': ['Hi', 'Hello', 'Goodby'],
            'col_3_dates': ['date'],
            'col_4_bool': [0,1],
            'col_5_int': [1,2,3,4,5,6,7,8,9],
            'col_6_num_range':['num_range']
            }
            
    # How many rows of data to generate 
    n = 200
    
    random_data = create_random_data(schema, n)
    
    name_out = 'random_data'
    
    # Save data 
    random_data.to_csv(name_out+'_'+str(n)+'.csv',index=False)  