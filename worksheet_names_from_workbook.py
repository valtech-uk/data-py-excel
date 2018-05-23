# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:11:30 2017

@author: downingj
"""

"""
Pull all worksheet names from excel files in folders
Save output to JSON format 
"""


def colate_sheets(top_path, output_path): 
    import os 
    import json 
    import xlrd as xr
    import glob

    # Find all .xlsx and .xls files 
    # Look recursively inside the folder 
    file_list_xlsx = glob.glob(top_path + '**/*.xlsx', recursive=True)
    file_list_xls = glob.glob(top_path + '**/*.xls', recursive=True)
    file_list = file_list_xlsx + file_list_xls

    # Create structured dataset 
    data_structured = {}
    for file in file_list:
        # Split filepaths 
        path, xls_filename = os.path.split(os.path.abspath(file))
        
        # Open excel 
        xls = xr.open_workbook(file, on_demand=True)
        
        # Grab sheet name data 
        xls_sheet_names = xls.sheet_names()
        
        # Release excel resources 
        xls.release_resources()
        
        # Add sheet names to dictionary 
        data_structured[xls_filename] = xls_sheet_names
    

    with open(output_path,'w') as f:
        tmp = json.dumps(data_structured,sort_keys=True, indent=4)
        f.write(tmp)
        
if __name__ == '__main__':
    
    # Which folder is at the top of our tree 
    top_path = '\path\here\\'
    
    # Name and / or Path + name to output file
    output_path = 'collated_headers.json'
    
    # Run the function    
    colate_sheets(top_path, output_path)
    