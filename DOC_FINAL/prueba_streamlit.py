import streamlit as st
import pandas as pd

st.title("Probando Streamlit  !!")
st.text("Este es el archivo meteorológico de Sevilla:")


df = pd.read_csv("sevilla_met.csv")

mes = st.number_input("Número del mes",min_value=1,max_value=12,value=1,step=1)
dia = st.number_input("Número del día",min_value=1,max_value=31,value=1,step=1)
st.write(dia,":",mes)
df_dia = df[(df["mes"] == mes) & (df["día"]==dia)]
st.dataframe(df_dia)
variable = st.selectbox("Variable a mostrar en la gráfica",df_dia.columns,index=3)
st.line_chart(df_dia,x="hora",y=[variable])