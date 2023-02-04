import streamlit as st
import src.soporte_imagenes as si
import src.soporte_datos as sd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("Volunteers by Age Groups")

df=sd.import_cleandata()

unicos=sd.unicos(df)

edad= sd.df_age(unicos)

edad_grupo=sd.bins(edad)

agrupado_edad=sd.group_by(edad_grupo,'Age_Group')

st.dataframe(agrupado_edad)

si.graf_barras("Age_Group","Total",agrupado_edad)

agrupado_temporal=sd.group_by2(edad,"Year","Age_Group")

st.write("Volunteers by Year & Age Groups")

st.dataframe(agrupado_temporal)

si.graf_historico1(agrupado_temporal,'Age_Group','Year','Total')
