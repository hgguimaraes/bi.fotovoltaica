# Importar Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carregar dados de geração, consumo e dados climaticos
geracao = pd.read_excel('dados_geracao.xlsx')
consumo = pd.read_excel('dados_consumo.xlsx')
clima = pd.read_excel('dados_clima.xlsx')

#Unir os dados em um único DataFrame com base na data:
dados = geracao.merge(consumo, on='data').merge(clima, on='data')

#Calcular a eficiência do painel solar com base na radiação solar e na temperatura:

dados['eficiencia'] = (dados['geracao'] / (dados['radiacao_solar'] * dados['temperatura'])) * 100

#Treinar um modelo de regressão linear com base nos dados de treinamento:

X = dados[['radiacao_solar', 'temperatura', 'consumo']]
y = dados['geracao']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

#Fazer predições com base nos dados de teste:

y_pred = modelo.predict(X_test)
#Avaliar o desempenho do modelo com base no coeficiente de determinação (R²):

plt.scatter(y_test, y_pred)
plt.plot([0, 600], [0, 600], '--', color='gray')
plt.xlabel('Geração real (W)')
plt.ylabel('Geração prevista (W)')
plt.show()

#Gráfico de linhas para visualizar a geração e o consumo de energia ao longo do tempo:

def exibir_dados(dados):
    st.write('## Dados')
    st.write(dados)

    st.write('## Gráfico de linhas')
    fig, ax = plt.subplots()
    ax.plot(dados['data'], dados['geracao'], label='Geração')
    ax.plot(dados['data'], dados['consumo'], label='Consumo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Energia (W)')
    ax.legend()
    st.pyplot(fig)

#Gráfico de dispersão para visualizar a relação entre a geração de energia fotovoltaica e os dados climáticos e de consumo:
def prever_energia(dados):
    X = dados[['radiacao_solar', 'temperatura', 'consumo']]
    y = dados['geracao']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    r2 = modelo.score(X_test, y_test)
    st.write(f"Coeficiente de determinação (R²): {r2:.2f}")

    st.write('## Gráfico de dispersão')
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.plot([0, 600], [0, 600], '--', color='gray')
    ax.set_xlabel('Geração real (W)')
    ax.set_ylabel('Geração prevista (W)')
    st.pyplot(fig)
