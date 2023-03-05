import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():
    # Título do aplicativo
    st.title("Análise de energia fotovoltaica")

    # Carrega os dados
    dados_geracao = pd.read_excel('dados_geracao.xlsx')
    dados_consumo = pd.read_excel('dados_consumo.xlsx')
    dados_climaticos = pd.read_excel('dados_climaticos.xlsx')

    # Exibe os dados
    exibir_dados(dados_geracao, dados_consumo, dados_climaticos)

    # Faz a previsão de energia
    prever_energia(dados_geracao, dados_consumo, dados_climaticos)

def exibir_dados(dados_geracao, dados_consumo, dados_climaticos):
    st.write('## Dados de geração')
    st.write(dados_geracao)

    st.write('## Dados de consumo')
    st.write(dados_consumo)

    st.write('## Dados climáticos')
    st.write(dados_climaticos)

def prever_energia(dados_geracao, dados_consumo, dados_climaticos):
    # Combina os dados de geração, consumo e climáticos
    dados = pd.merge(dados_geracao, dados_consumo, on='data')
    dados = pd.merge(dados, dados_climaticos, on='data')

    # Divide os dados em conjuntos de treinamento e teste
    X = dados[['radiacao_solar', 'temperatura', 'consumo']]
    y = dados['geracao']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Cria e ajusta o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Faz a previsão de energia e exibe o coeficiente de determinação
    y_pred = modelo.predict(X_test)
    r2 = modelo.score(X_test, y_test)
    st.write(f"Coeficiente de determinação (R²): {r2:.2f}")

    # Exibe o gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.plot([0, 600], [0, 600], '--', color='gray')
    ax.set_xlabel('Geração real (W)')
    ax.set_ylabel('Geração prevista (W)')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
