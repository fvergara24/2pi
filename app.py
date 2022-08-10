import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import altair as alt
from PIL import Image



image = Image.open('Henry.jpg')
                            
st.image(image)

st.title("PI2 Fernando Vergara")

st.write('dfhola noseendoneestas')


st.write('Tabla 1. Estados con mayor ocupación hospitalario por COVID-19 en los primeros 6 meses del 2020')
#df=pd.read_csv('https://raw.githubusercontent.com/soyHenry/DS-PI-ProyectoIndividual/main/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
df=pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
df.date=pd.to_datetime(df.date, format='%Y/%m/%d')

mask = (df['date'] > '2020/1/1') & (df['date'] <= '2020/6/30')
df1=df.loc[mask]

#PUNTO 1
df3_6meses=df1[['date','state','total_adult_patients_hospitalized_confirmed_covid','total_pediatric_patients_hospitalized_confirmed_covid']].copy()
df3_6meses.reset_index(inplace=True, drop=True)
df3_6meses.rename(columns={'total_adult_patients_hospitalized_confirmed_covid':'Total Adult','total_pediatric_patients_hospitalized_confirmed_covid':'Total Pediatric'}, inplace=True)
df3_6meses= df3_6meses.fillna(0, axis=1)
df3_6meses['Total']=df3_6meses['Total Adult']+df3_6meses['Total Pediatric']
top5_3 = df3_6meses.groupby('state').sum()
top5_3 = top5_3.sort_values(by=['Total'],inplace=False, ascending=False)
st.dataframe(data=top5_3, width=None, height=None)

st.write('Tabla 2. Total de ocupación hospitalaria por COVID-19 por mes')                            
st.image(Image.open('meses.jpg'))

#PUNTO 2
df2_todas=df[['date','state','inpatient_beds_used_covid']].copy()
df2_todas=df2_todas[df2_todas['state']=='NY']
df2_todas=df2_todas.drop('state',axis=1)

#ALTAIR
# generate a date range to be used as the x axis
df_melted = pd.melt(df2_todas, id_vars='date', var_name='Fecha', value_name='Cantidad de camas')
c = alt.Chart(df_melted, title='Ocupación de camas en el estado de Nueva York').mark_point().encode(x='Fecha', y='Cantidad de camas')#, color='parameter')
st.altair_chart(c, use_container_width=True)


#PUNTO 3
mask3 = (df['date'] >= '2020/1/1') & (df['date'] <= '2020/12/31')
df3=df.loc[mask3]
df3=df3[['date','state','staffed_icu_adult_patients_confirmed_covid']].copy()
df3.reset_index(inplace=True, drop=True)
df3=df3.groupby('state').sum().sort_values(by='staffed_icu_adult_patients_confirmed_covid',ascending=False).head(5)
df3=df3.rename(columns={'staffed_icu_adult_patients_confirmed_covid':'Total Camas UCI'}, inplace=False)
st.dataframe(data=df3, width=None, height=None)


#PUNTO 7
df7=df[['date','state','deaths_covid','critical_staffing_shortage_today_yes']].copy()
mask2021=(df['date'] >= '2021/1/1') & (df['date'] <= '2021/12/31')
df7=df7.loc[mask2021]
df7.reset_index(inplace=True, drop=True)
df7=df7.rename(columns={'deaths_covid':'Muertes Covid','critical_staffing_shortage_today_yes':'Falta de Personal'}, inplace=False)
df7=df7.dropna()
df7=df7.groupby('state').sum()
#Gráfica
x7=df7['Falta de Personal']
y7=df7['Muertes Covid']
