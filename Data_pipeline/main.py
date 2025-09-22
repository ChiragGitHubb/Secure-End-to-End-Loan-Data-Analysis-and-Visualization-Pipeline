# main.py

# importing all libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import regex as re
import warnings
warnings.filterwarnings('ignore')

# importing all files
from data_loader import data_loader as dl
from data_cleaner import data_cleaner as dc
from data_processor import data_processor as dp
from data_visualizer import data_visualizer as dv
from data_saver import data_saver as ds

# importing all data and paths
file_path=r"D:\Case Study Python\Case Study 1 Loan Data\Data_pipeline\input_data\Loan Data.csv"
output_file_path=r"D:\Case Study Python\Case Study 1 Loan Data\Data_pipeline\output_data"

# irrevalant columns in the data
irrevalant_cols=['id', 'state', 'inquiries_in_the_last_6_months']

# main program
if __name__=='__main__':
    print('Pipeline started')
    print('-----Data loading phase going on-----\n')
    df=dl.load_data(file_path)
    if df is None:
        exit()
    print('-----Data is loaded successfully-----\n')
    print('-----Data cleaning phase going on-----\n')
    df=dc.columns_headings_fix(df)
    df=dc.removing_irrevalant_columns(df,irrevalant_cols)
    df=dc.fixing_columns_values(df)
    print(df)
    print('-----Data is cleaned successfully-----\n')
    print('-----Data processing phase going on-----\n')
    df=dp.handling_missing_values(df)
    df=dp.filling_missing_values(df)
    df,num_data=dp.data_encoding(df)
    print('-----Data is processed successfully-----\n')
    print('-----Data visualization phase going on-----\n')
    df=dv.fixing_the_ouliners(df)
    df=dv.plotting_data(df,num_data)
    print('-----Data visualized successfully-----\n')
    print('-----Data saving phase going on-----\n')
    df=ds.data_save(df,output_file_path,file_path)
    print('-----Data saved successfully-----\n')
    