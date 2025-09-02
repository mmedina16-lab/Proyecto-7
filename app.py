import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header("Análisis de Vehículos")

df = pd.read_csv("vehicles_us.csv")

if st.button("Construir histograma del odómetro"):
    st.write("Creación de un histograma para el odómetro de los vehículos")
    fig_hist = go.Figure(data=[go.Histogram(x=df["odometer"])])
    fig_hist.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

if st.button("Construir scatter plot precio vs odómetro"):
    st.write("Creación de un gráfico de dispersión entre precio y odómetro")
    fig_scatter = go.Figure(data=[go.Scatter(x=df["odometer"], y=df["price"], mode="markers")])
    fig_scatter.update_layout(title_text="Precio vs Odómetro")
    st.plotly_chart(fig_scatter, use_container_width=True)
    


