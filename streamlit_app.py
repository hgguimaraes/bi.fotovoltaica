{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1015c5f9-020d-40e7-b575-066c7ab7f629",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "import streamlit as st\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "51038176-fcac-48e7-afae-b9bf951aebb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Carregando os dados do arquivo Excel\n",
    "df_energia = pd.read_excel('dados_energia.xlsx')\n",
    "df_clima = pd.read_excel('dados_clima.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "9c534af5-8302-49d4-a006-40019d5e30a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criando uma tabela dinâmica para os dados de energia\n",
    "df_pivot_energia = pd.pivot_table(df_energia, index=['Mês'], values=['Geração', 'Compensação'], aggfunc='sum')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "1fff8bba-3bf2-4faf-90c8-41dfe6dfaecb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Criando gráficos com plotly\n",
    "fig_energia = px.bar(df_pivot_energia, x=df_pivot_energia.index, y=['Geração', 'Compensação'], title='Energia Fotovoltaica')\n",
    "fig_temperatura = px.line(df_clima, x='Mês', y='Temperatura', title='Temperatura')\n",
    "fig_chuva = px.bar(df_clima, x='Mês', y='Chuva', title='Chuva')\n",
    "fig_irradiancia = px.line(df_clima, x='Mês', y='Irradiancia', title='Irradiancia')\n",
    "fig_humidade = px.line(df_clima, x='Mês', y='Humidade', title='Humidade')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "2d75dae4-66f6-4182-966b-a6ccbc0dfc99",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-02-23 09:20:54.491 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\hg_gu\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Criando a interface do usuário com streamlit\n",
    "st.title('Análise de Energia Fotovoltaica e Dados Climáticos')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "520598b9-2416-481a-845f-9988de359ea6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Seleção de gráficos\n",
    "option = st.sidebar.selectbox('Selecione o gráfico:', ['Energia Fotovoltaica', 'Temperatura', 'Chuva', 'Irradiancia', 'Humidade'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "423d7fe2-5b05-4402-ba67-367c6ea47a64",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exibindo o gráfico selecionado\n",
    "if option == 'Energia Fotovoltaica':\n",
    "    st.plotly_chart(fig_energia)\n",
    "elif option == 'Temperatura':\n",
    "    st.plotly_chart(fig_temperatura)\n",
    "elif option == 'Chuva':\n",
    "    st.plotly_chart(fig_chuva)\n",
    "elif option == 'Irradiancia':\n",
    "    st.plotly_chart(fig_irradiancia)\n",
    "else:\n",
    "    st.plotly_chart(fig_humidade)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2be02a69-426c-4084-a244-712d5fa138bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
