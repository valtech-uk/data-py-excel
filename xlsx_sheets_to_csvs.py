# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:13:30 2017

@author: downingj
"""

"""
Split all sheets within a workbook to csv files
"""

def xlsx_sheets_to_csv(xlsx_path):
    import xlrd as xr
    import pandas as pd

    # Open excel 
    xls = xr.open_workbook(xlsx_path, on_demand=True)
    
    # Grab sheet name data 
    xlsx_sheet_names = xls.sheet_names()

    # Open each sheet and save required headers 
    for sheet in xlsx_sheet_names:
        try:
            # Open sheet 
            data = pd.read_excel(xlsx_path, sheetname=sheet, skiprows=1)
                        
            # drop empty rows -- sometimes there are many at the bottom
            data.dropna(how='all', inplace=True)
            
            # Save to CSV 
            path_out = xlsx_path[:-5] + '_' + sheet + '.csv'
            path_out = path_out.lower().replace(' ','_')
            
            # Save but don't write the index which is added by pandas 
            data.to_csv(path_out, index=False)
            print('Saved: %s' %sheet)
        except:
            print('Unable to process, sheet: %s' %sheet)

if __name__ == '__main__':
    
    # Path to stage data 
    xlsx_path = 'my_data.xlsx'
    
    # Run the function
    xlsx_sheets_to_csv(xlsx_path)



        




        
