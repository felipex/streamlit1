import streamlit as st
import requests

unidade = "122391"  #UFCA
#estrutura = requests.get(
#    f"http://estruturaorganizacional.dados.gov.br/doc/unidade-#organizacional/{unidade}/estrutura"
#)
estrutura = requests.get(
    #"https://estruturaorganizacional.dados.gov.br/doc/unidade-organizacional/122391/completa"
    "https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/resumida?codigoPoder=1&codigoEsfera=1&codigoUnidade=122391"
)

estrutura = estrutura.json()

st.title("Estrutura Organizacional da UFCA")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/8/8e/Logomarca_UFCA.svg",
    width=100)
st.write(
    "Dados obtidos do [Portal da Transparência](http://www.portaltransparencia.gov.br"
)
st.write(estrutura)
