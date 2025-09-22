import numpy as np
import pandas as pd
def handling_missing_values(df):
    df.isna().sum()
    df.dropna(inplace=True)
    return df

def filling_missing_values(df):
    # declaring numerical and categorical columns
    num_cols=['amount_requested', 'amount_funded_by_investors', 'interest_rate','debt_to_income_ratio','monthly_income', 'fico_range', 'open_credit_lines', 'revolving_credit_balance']
    cat_cols=[col for col in df.columns if col not in num_cols]
    def impute_with_mean(col):
        df[col]=df[col].fillna(df[col].mean())
    for col in num_cols:
        impute_with_mean(col)
    def impute_with_mode(col):
        df[col]=df[col].fillna(df[col].mode().iloc[0])
    for col in cat_cols:
        impute_with_mode(col)
    return df

def data_encoding(df):
    # Splitting the data into numeric
    num_df=df.select_dtypes(include='number')
    # Splitting the data into non numeric
    obj_df=df.select_dtypes(include='object')
    # Applying Label encoding for loan purpose 
    obj_df.loan_purpose=obj_df.loan_purpose.astype('category').cat.codes
    # Applying One hot encoding for home ownership 
    obj_df=pd.get_dummies(obj_df, columns=['home_ownership'],dtype=int)
    # Concatenate numeric and non numeric data types along a axis
    num_data=pd.concat((num_df, obj_df), axis=1)
    # Checking concatenated data types
    num_data.dtypes
    return df,num_data