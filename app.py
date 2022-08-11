import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import altair as alt
from PIL import Image



image = Image.open('Henry.jpg')
                            
st.image(image)

st.title("PI2 Fernando Vergara")
## PI2 Fernando Vergara

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

#PUNTO 2
df2_todas=df[['date','state','inpatient_beds_used_covid']].copy()
df2_todas=df2_todas[df2_todas['state']=='NY']
df2_todas=df2_todas.drop('state',axis=1)
#Gráfica
#ALTAIR
# generate a date range to be used as the x axis
df_melted = pd.melt(df2_todas, id_vars='date', value_name='Cantidad de camas')
c = alt.Chart(df_melted, title='Ocupación de camas en el estado de Nueva York').mark_point().encode(x='date', y='Cantidad de camas').interactive()
st.altair_chart(c, use_container_width=True)


#PUNTO 3
mask3 = (df['date'] >= '2020/1/1') & (df['date'] <= '2020/12/31')
df3=df.loc[mask3]
df3=df3[['date','state','staffed_icu_adult_patients_confirmed_covid']].copy()
df3.reset_index(inplace=True, drop=True)
df3=df3.groupby('state').sum().sort_values(by='staffed_icu_adult_patients_confirmed_covid',ascending=False).head(5)
df3=df3.rename(columns={'staffed_icu_adult_patients_confirmed_covid':'Total Camas UCI'}, inplace=False)
st.dataframe(data=df3, width=None, height=None)

#PUNTO 4
df4=df[['date','state','total_pediatric_patients_hospitalized_confirmed_covid']].copy()
mask_2020 = (df['date'] >= '2020/1/1') & (df['date'] <= '2020/12/31')
df4=df4.loc[mask_2020]
df4.reset_index(inplace=True, drop=True)
df4=df4.rename(columns={'total_pediatric_patients_hospitalized_confirmed_covid':'Total Camas Pediátricas'}, inplace=False)
df4=df4.dropna()
df4=df4.groupby('state').sum().sort_values(by='Total Camas Pediátricas',ascending=False).head(5)
st.dataframe(data=df4, width=None, height=None)

#PUNTO 5
df5=df[['date','state','total_staffed_adult_icu_beds','staffed_icu_adult_patients_confirmed_covid']].copy()
mask5 = (df['date'] <= '2021/8/1')
df5=df5.loc[mask5]
df5.reset_index(inplace=True, drop=True)
df5=df5.rename(columns={'total_staffed_adult_icu_beds':'Total Camas ICU','staffed_icu_adult_patients_confirmed_covid':'Total Camas ICU Confirmada'}, inplace=False)
df5=df5.dropna()
df5.drop(df5[(df5['Total Camas ICU']==0) & (df5['Total Camas ICU Confirmada']==0)].index, inplace=True)
df5=df5.groupby('state').sum()
df5['%']=round(df5['Total Camas ICU Confirmada']*100/df5['Total Camas ICU'],2)
df5=df5.sort_values(by='%',ascending=False).head(5)
st.dataframe(data=df5, width=None, height=None)

#PUNTO 6
df6=df[['date','state','deaths_covid']].copy()
mask2021=(df['date'] >= '2021/1/1') & (df['date'] <= '2021/12/31')
df6=df6.loc[mask2021]
df6.reset_index(inplace=True, drop=True)
df6=df6.rename(columns={'deaths_covid':'Muertes Covid'}, inplace=False)
df6=df6.dropna()
df6=df6.groupby('state').sum()
df6=df6.sort_values(by='Muertes Covid',ascending=False).head(5)
st.dataframe(data=df6, width=None, height=None)

#PUNTO 7
df7=df[['date','state','deaths_covid','critical_staffing_shortage_today_yes']].copy()
mask2021=(df['date'] >= '2021/1/1') & (df['date'] <= '2021/12/31')
df7=df7.loc[mask2021]
df7.reset_index(inplace=True, drop=True)
df7=df7.rename(columns={'deaths_covid':'Muertes Covid','critical_staffing_shortage_today_yes':'Falta de Personal'}, inplace=False)
df7=df7.dropna()
df7=df7.groupby('state').sum()

#Gráfica
df_melted_7 = pd.melt(df7, id_vars='Falta de Personal', value_name='Muertes Covid')
c_7 = alt.Chart(df_melted_7, title='Relación entre Falta de Personal y Muertes por Covid-19').mark_point().encode(x='Falta de Personal', y='Muertes Covid').interactive()#, color='parameter')
st.altair_chart(c_7, use_container_width=True)

## PUNTO 1.  y PUNTO 3. DEL DASHBOARD
st.write('Mapa que muestre la cantidad de hospitalizados debido al COVID-19 por Estado.')
dfmap = df[['state','total_adult_patients_hospitalized_confirmed_covid']].copy()
dfmap.rename(columns={'total_adult_patients_hospitalized_confirmed_covid':'Total Adult'}, inplace=True)
dfmap = dfmap.fillna(0, axis=1)
dfmap = dfmap.groupby('state', as_index=False, sort=False).sum()
df_melted_8 = pd.melt(dfmap, id_vars='state', value_name='Total Adult')
c_8 = alt.Chart(df_melted_8, title='Total de hospitalizados por COVID-19').mark_point().encode(x='state', y='Total Adult').interactive()
st.altair_chart(c_8, use_container_width=True)

## PUNTO 2. DASHBOARD
st.write('Grafica. Cantidad de Camas UCI por estado')
dfd2=df[['date','state','staffed_icu_adult_patients_confirmed_covid']].copy()
dfd2.reset_index(inplace=True, drop=True)
dfd2=dfd2.groupby('state').sum().sort_values(by='staffed_icu_adult_patients_confirmed_covid',ascending=False).head(5)
dfd2=dfd2.rename(columns={'staffed_icu_adult_patients_confirmed_covid':'Total Camas UCI'}, inplace=False)
st.dataframe(data=dfd2, width=None, height=None)