import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Autos Electricos",
    page_icon="🚕",
    layout="wide",
)

@st.cache_data
def get_data() -> pd.DataFrame:
        df= pd.read_csv('ElectricCarData_Clean.csv')
        return df

df = get_data()
st.dataframe(df)

#----------------------------------------------------------------
Brand_car = st.selectbox("Selecciona la Marca", pd.unique(df["Brand"]))

placeholder = st.empty()
# Crear los KPIs

df = df[df['Brand']==Brand_car]

for seconds in range(200):
        df['Efficiency_WhKm'] = df['Efficiency_WhKm'] * np.random.uniform(0.9, 1.1)        
        df['Range_Km'] = df['Range_Km'] * np.random.uniform(0.9, 1.1)

# Crear kpi 
        eficiencia = np.mean(df['Efficiency_WhKm']) 

        kilometros = int(df[(df["Range_Km"]=='Efficiency_WhKm')]['Range_Km'].count() + np.random.uniform(0.9, 1.1))
        
        with placeholder.container():
        # create three columns
                kpi1, kpi2 = st.columns(2)

# filtrar en estos kpi 
        
kpi1.metric(label="Eficiencia👌", value=round(eficiencia), delta= round(eficiencia) - 10)
kpi2.metric(label="Kilometros ☝️", value=int(df['Range_Km'].mean()), delta=-10 + int(df['Range_Km'].mean()) - round(df['Range_Km'].mean()/eficiencia) * 100)
 # create two columns for charts 

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
        st.markdown("### Primer Grafico")
        fig = px.density_heatmap(data_frame=df, y='Efficiency_WhKm', x='Range_Km')        
        st.write(fig)
        with fig_col2:
                st.markdown("### Segundo Grafico")
                fig2 = px.histogram(data_frame = df, x = 'AccelSec')               
                st.write(fig2)
                st.markdown("### Detalles de los datos")
                st.dataframe(df)
                time.sleep(1)
                #placeholder.empty()