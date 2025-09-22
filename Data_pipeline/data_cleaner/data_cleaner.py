import pandas as pd
import numpy as np
def columns_headings_fix(df):
    df.columns=df.columns.str.replace('.','_').str.lower()
    return df
def removing_irrevalant_columns(df,irrevalant_cols):
    df.drop(columns=irrevalant_cols, inplace=True)
    return df
def fixing_columns_values(df):
    # amount_requested 
    df.loc[df.amount_requested=='.', 'amount_requested']=np.nan
    df.amount_requested=df.amount_requested.astype(float)
    # amount_funded_by_investor 
    df.amount_funded_by_investors=pd.to_numeric(df.amount_funded_by_investors, errors='coerce')
    # interest_rate
    df.interest_rate=df.interest_rate.str.strip('%').astype(float)
    # loan_length
    df.loan_length=pd.to_numeric(df.loan_length.str.strip(' months'), errors='coerce')
    # debt_to_income_ratio
    df.debt_to_income_ratio=pd.to_numeric(df.debt_to_income_ratio.str.strip('%'), errors='coerce')
    # fico_range
    def clean_fico_range(val):
        low, high=val.split('-')
        low=int(low)
        high=int(high)
        return (low+high)/2
    df.fico_range=df.fico_range.apply(clean_fico_range)
    # open_credit_lines
    df.open_credit_lines=pd.to_numeric(df.open_credit_lines, errors='coerce')
    # revoling_credit
    df.revolving_credit_balance=pd.to_numeric(df.revolving_credit_balance, errors='coerce')
    # employment_length
    df.employment_length=pd.to_numeric(df.employment_length.replace({'10+ years':11, '< 1 year':.5}).replace(r'[^0-9.]', '', regex=True), errors='coerce')
    return df