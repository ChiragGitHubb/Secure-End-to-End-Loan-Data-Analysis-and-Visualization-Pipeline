import os
import pandas as pd

def data_save(df, output_file_path, file_path):
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        new_file_path=os.path.join(output_file_path, 'Final.xslx')
        df.to_excel(new_file_path, index=False)
        print(f'File is saved at -{file_path}')
    elif file_path.endswith('.csv'):
        new_file_path=os.path.join(output_file_path, 'Final.csv')
        df.to_csv(new_file_path, index=False)
        print(f'File is saved at-{file_path}')
    else:
        print('Invalid file type')
    return df