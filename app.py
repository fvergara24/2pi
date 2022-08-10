import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



image = Image.open('Henry.jpg')
                            
st.image(image)

st.title("PI2 Fernando Vergara")




df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)


st.write('dfhola noseendoneestas')




#df=pd.read_csv('https://raw.githubusercontent.com/soyHenry/DS-PI-ProyectoIndividual/main/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
df=pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
df.date=pd.to_datetime(df.date, format='%Y/%m/%d')
mask = (df['date'] > '2020/1/1') & (df['date'] <= '2020/6/30')
df1=df.loc[mask]
df3_6meses=df1[['date','state','total_adult_patients_hospitalized_confirmed_covid','total_pediatric_patients_hospitalized_confirmed_covid']].copy()
df3_6meses.reset_index(inplace=True, drop=True)
df3_6meses.rename(columns={'total_adult_patients_hospitalized_confirmed_covid':'Total Adult','total_pediatric_patients_hospitalized_confirmed_covid':'Total Pediatric'}, inplace=True)
df3_6meses= df3_6meses.fillna(0, axis=1)
df3_6meses['Total']=df3_6meses['Total Adult']+df3_6meses['Total Pediatric']
top5_3 = df3_6meses.groupby('state').sum()
top5_3 = top5_3.sort_values(by=['Total'],inplace=False, ascending=False)
st.dataframe(data=top5_3, width=None, height=None)