"""
@author: jondowning
"""

import pandas as pd 
import glob 

def aggregate_excel_data(xlsx_file_list, xlsx_sheet_name):
    
    aggregated_data = pd.DataFrame()
    
    for file in xlsx_file_list:
        try: 
            data = pd.read_excel(file, sheet_name = xlsx_sheet_name, skiprows = 0)
            aggregated_data = pd.concat([aggregated_data, data], axis=0)
        except: 
            print('sheet name (%s) doesn\'t exist in file: %s' %(xlsx_sheet_name, file))
            
    return aggregated_data
                
        
if __name__ == '__main__':
    
    # Path to data 
    path_to_data = './path/data'
    
    # Sheet name
    xlsx_sheet_name = 'sheetname'
    
    # path for data out
    path_out = 'aggregated_xlsx_data'
    
    # Find excel files: 
    xlsx_file_list = glob.glob(path_to_data + '**/*.xlsx', recursive=True)
    
    # Run the function
    aggregated_data = aggregate_excel_data(xlsx_file_list, xlsx_sheet_name)
    
    # Save data to CSV
    aggregated_data.to_csv(path_out + '.csv', index=False)

    
    