import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/fherponce/Proyecto-Sprint5/vehicles_us.csv')
st.header('Welcome to my Project')  # crear el encabezado
hist_button = st.button('Construir un histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear el segundo botón
graphic_button = st.button('Construir un Gráfico de Dispersión')

if graphic_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
