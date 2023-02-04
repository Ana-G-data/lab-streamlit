import pandas as pd
import streamlit as st
import src.soporte_datos as sd


def import_cleandata():
    df = pd.read_csv('datos/volunteers_1v.csv', low_memory=False)
    df.columns= df.columns.str.lstrip()
    df.columns= df.columns.str.rstrip()
    df.columns = df.columns.str.replace(" ", "_")
    df["Anglo_Status"].fillna("TBC", inplace=True)
    df['Veteran'].fillna("No",inplace=True) 
    df['Year'] = df['Course'].str.extract(r'(\d{4})')
    df=df.dropna(subset='Date_Modified')
    df.drop(['Course','Arrival_Medium','Arrival_Company','Arrival_Number','Birth_Date'],axis=1,inplace=True)
    df = df.rename(columns={'Date_Modified.1': 'Date_Modified1'})
    df['Year'].fillna(method='ffill', inplace=True)
    df['Year'].isnull().sum()
    return df  

def unicos(df):
    df.drop_duplicates(subset='Name', inplace=False)
    df.drop(['Anglo_Status','Date_Modified','Request_Status','Date_Modified1'],axis=1,inplace=True)
    df['Age'].astype(int)
    return df

def df_age(df):
    df[df['Age'] >= 18]
    df_edad_totales=df[df['Age']>=18]
    return df

def bins(df):
    bins_age = [17, 25, 40, 60, 75, df['Age'].max()]
    labels_age = ['18-25', '26-40', '41-60', '61-75', '76+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins_age, labels=labels_age)
    return df

def group_by(df,columna):
    return df.groupby([columna]).size().reset_index(name='Total')

def group_by2(df,columna1,columna2):
    df=df.groupby([columna1, columna2]).sum().reset_index()
    df.columns=['Year','Age_Group','Total']
    return df
    