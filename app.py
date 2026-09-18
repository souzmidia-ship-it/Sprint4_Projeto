import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Aplicativo para análise de venda de veículos')

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
st.write("A maioria dos carros tem menos de 100 mil milhas rodadas.")

scatter_button = st.button('Criar gráfico de dispersão') # criar um botão
        
if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
    st.write("Existe uma relação inversa entre quilometragem e preço: carros com maior quilometragem tendem a apresentar preços menores.")

