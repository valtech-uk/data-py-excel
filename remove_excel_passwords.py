# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:55:50 2017

@author: downingj
"""

'''
Open all xlsx files and remove a set password 
'''

def unprotect_xlsx(password_str, filename_in, filename_out):
    import win32com.client
    
    # Open excel 
    xcl = win32com.client.Dispatch('Excel.Application')

    # Open file in excel, applying the password
    wb = xcl.Workbooks.Open(filename_in, False, True, None, password_str)

    # Remove alerts 
    xcl.DisplayAlerts = False
    
    # Save the files to our put path 
    wb.SaveAs(filename_out, None, '', '')
    
    # Close excel 
    xcl.Quit()



if __name__ == '__main__':
    import os
    import glob

    # Which folder is at the top of our tree 
    top_path = r'\user\xlxs_path'
    
    # Which password do we want to use 
    password_str = 'hello'
    
    # Find all .xlsx and .xls files 
    # Look recursively inside the folder 
    file_list_xlsx = glob.glob(top_path + '**/*.xlsx', recursive=True)
    file_list_xls = glob.glob(top_path + '**/*.xls', recursive=True)
    file_list = file_list_xlsx + file_list_xls
        
    for file in file_list:
        filename_out = file[:-5] + '_no_pw.xlsx'
        unprotect_xlsx(password_str, file, filename_out)
        
        # Delete original file (the one with the password..)
        os.remove(file)

        
    