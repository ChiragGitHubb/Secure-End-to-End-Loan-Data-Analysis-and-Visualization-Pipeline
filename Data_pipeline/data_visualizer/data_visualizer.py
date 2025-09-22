import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

num_cols=['amount_requested', 'amount_funded_by_investors', 'interest_rate','debt_to_income_ratio','monthly_income', 'fico_range', 'open_credit_lines', 'revolving_credit_balance']
  
def fixing_the_ouliners(df):
    def cap_outliers(col):
        print(col)
        q1=df[col].quantile(.25)
        q3=df[col].quantile(.75)
        iqr=q3-q1
        lower=q1-1.5*iqr
        upper=q3+1.5*iqr
        df[col]=df[col].clip(lower, upper)
    num_cols=['amount_requested', 'amount_funded_by_investors', 'interest_rate','debt_to_income_ratio','monthly_income', 'fico_range', 'open_credit_lines', 'revolving_credit_balance']
    for col in num_cols:
        cap_outliers(col)
    return df

def plotting_data(df,num_data):
    # plotting the box plot
    f,a=plt.subplots(2,4, figsize=(15,10), dpi=100)
    ind=0
    for i in range(2):
        for j in range(4):
            sns.boxplot(data=df, y=num_cols[ind], ax=a[i,j])
            ind+=1
        plt.tight_layout()
    plt.show()
    # plotting the correlation
    plt.figure(figsize=(15,12), dpi=100)
    sns.heatmap(num_data.corr(), annot=True, fmt='.2f')
    plt.show()
    return df