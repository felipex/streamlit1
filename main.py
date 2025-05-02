import streamlit as st
import requests

unidade = "122391" #UFCA

estrutura = requests.get(f"http://estruturaorganizacional.dados.gov.br/doc/unidade-organizacional/{unidade}/estrutura")
estrutura = estrutura.json()
st.write(estrutura)
