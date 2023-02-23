import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados do arquivo Excel
df_energia = pd.read_excel('dados_energia.xlsx', sheet_name='energia')
df_clima = pd.read_excel('dados_clima.xlsx', sheet_name='clima')

# Criando uma tabela dinâmica para os dados de energia
df_pivot_energia = pd.pivot_table(df_energia, index=['Mês'], values=['Geração', 'Compensação'], aggfunc='sum')

# Criando gráficos com plotly
fig_energia = px.bar(df_pivot_energia, x=df_pivot_energia.index, y=['Geração', 'Compensação'], title='Energia Fotovoltaica')

fig_temperatura = px.line(df_clima, x='Mês', y='Temperatura', title='Temperatura')
fig_chuva = px.bar(df_clima, x='Mês', y='Chuva', title='Chuva')
fig_irradiancia = px.line(df_clima, x='Mês', y='Irradiancia', title='Irradiancia')
fig_humidade = px.line(df_clima, x='Mês', y='Humidade', title='Humidade')

# Criando a interface do usuário com streamlit
st.title('Análise de Energia Fotovoltaica e Dados Climáticos')

# Seleção de gráficos
option = st.sidebar.selectbox('Selecione o gráfico:', ['Energia Fotovoltaica', 'Temperatura', 'Chuva', 'Irradiancia', 'Humidade'])

# Exibindo o gráfico selecionado
if option == 'Energia Fotovoltaica':
    st.plotly_chart(fig_energia)
elif option == 'Temperatura':
    st.plotly_chart(fig_temperatura)
elif option == 'Chuva':
    st.plotly_chart(fig_chuva)
elif option == 'Irradiancia':
    st.plotly_chart(fig_irradiancia)
else:
    st.plotly_chart(fig_humidade)
