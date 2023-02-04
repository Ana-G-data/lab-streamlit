import pandas as pd
import numpy as np
import streamlit as st
import re
pd.options.display.max_columns = None
from datetime import datetime, date
from datetime import datetime, time, timedelta
import warnings
import matplotlib.pyplot as plt
import requests
import os 
import seaborn as sns
from dotenv import load_dotenv
load_dotenv()

def graf_barras(userx, usery, data):
    fig, ax = plt.subplots(figsize=(30, 10))
    sns.barplot(x=userx, y=usery, data=data, ax=ax)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    st.pyplot(fig)

def graf_historico1(df,col1,col2,col3):
    fig, axs = plt.subplots(1, figsize=(20, 10))
    
    for group in df[col1].unique():
        subset = df[df[col1] == group]
        plt.plot(subset[col2], subset[col3], label=group)
    plt.xlabel(col2)
    plt.ylabel(col3)
    plt.legend()
    
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    st.pyplot(fig)
    

        


