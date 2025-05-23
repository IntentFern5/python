import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

apgn = pd.read_csv('datos_anteproyecto.csv')
ran = pd.read_csv('datos_random.csv')

st.title("Aplicación 2")

tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])


with tab1:
    #analisis univariado
    fig, ax = plt.subplots(1, 3, figsize = (10, 4))

    # educ
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values, color = 'yellow')  # grafico de barras y siempre necesitare la tabla de frecuencias, que es el renglon anterior

    # edad
    ax[1].hist(ran['edad'], bins = 40, color = 'red') # histograma 

    # wage
    ax[2].hist(ran['wage'], bins = 40, color = 'skyblue')

    st.pyplot(fig)

    # analisis bivariado
    fig, ax = plt.subplots(1, 2, figsize = (10, 4)) # 1, 2 es 1 fila 2 columnas

    # educ vs. wage
    ax[0].scatter(ran['educ'], ran['wage'], color = 'orange') # grafico de dispersión

    # edad vs. wage
    ax[1].scatter(ran['edad'], ran['wage'], color = 'black')

    st.pyplot(fig)


with tab2:
   fig = px.treemap(data_frame=apgn, path=[px.Constant("PGN"), 'Nombre Sector', 'Tipo de gasto'], values='Valor', color = 'Valor', color_continuous_scale = 'oranges')

   st.plotly_chart(fig)