# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:33:31 2017

@author: downingj
"""

"""
Aggregate CSV headers to JSON 
"""

def csv_headers_to_json(folder_in, json_file_out):
    import glob
    import os 
    import pandas as pd
    import json 
    
    filepaths = glob.glob(folder_in + '**\*.csv', recursive=True)
    
    header_dict = {}

    # Setup our dictionary for structuring the data     
    for file in filepaths:
        path, filename = os.path.split(os.path.abspath(file))
        header_dict[path] = {}
      
        
    for file in filepaths: 
        path, filename = os.path.split(os.path.abspath(file))
        filename = os.path.basename(file)
        try:
            data = pd.read_csv(file)
            col = list(data.columns)
            header_dict[path][filename[:-4]] = col 
        except:
            pass

    with open(json_file_out, 'w') as f:
        json.dump(header_dict, f, indent=4, sort_keys=True)
    
if __name__ == '__main__':

    # Which folder do we want to examine
    folder_in = r'\path\here\\'
    
    # Where to save outputs
    json_file_out = r'my_headers.json'


