import pandas as pd
def load_data(file_path):
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df=pd.read_excel(file_path)
        return df
    elif file_path.endswith('.csv'):
        df=pd.read_csv(file_path)
        return df
    else:
        print('Invalid File type')
        print('Takes only excel or csv files!')
        return None