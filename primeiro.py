import pandas as pd
import streamlit as st
from requests import get
url_api_bovespa = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4334/dados?formato=json"
def carregar_siglas():
    """
    Função para carregar as siglas da bolsa da Ibovespa

    Retorna:
        DataFrame com as siglas e os nomes das empresas
    """
    
    resposta = get(url_api_bovespa)
    dados = resposta.json()
    
    df_siglas = pd.DataFrame(dados["series"][0]["dados"])
    df_siglas.columns = ["data", "sigla", "valor"]
    
    return df_siglas[["sigla", "valor"]]

df_siglas = carregar_siglas()

st.title("Ibovespa - Selecione a Sigla")

sigla_selecionada = st.checkbox("Mostrar valor", value=False)

if sigla_selecionada:
    st.write(df_siglas.to_html())
