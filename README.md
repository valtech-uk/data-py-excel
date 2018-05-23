# Common functions for dealing with Excel


## remove_excel_passwords.py
Often we have very many password protected excel documents. ```remove_excel_passwords.py``` removes the password from all documents stored in a folder 

## worksheet_names_from_workbook.py
Some workbooks have 100 worksheets, this scrapes the worksheet names into one JSON

## xlsx_sheets_to_csv.py
Sometimes splitting every XLSX to a CSV is helpful, especially for loading things onto HDFS

## csv_headers_to_json.py
Aggregating the headers from a CSV to a JSON is great to find the overlaps for joining many tables 

## join_excel_to_csv.py
Join many of the same excel sheets across different workbooks into a CSV. 

## create_random_data.py
With a defined schema, generate random values

## clean_data_common_functions.py
Common data cleaning functions and examples for pandas 