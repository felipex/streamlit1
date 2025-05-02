import streamlit as st
import requests
import pandas as pd
import json

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
#st.write(estrutura)

#################
unidade = "122391"  #UFCA

estrutura = requests.get(
    f"http://estruturaorganizacional.dados.gov.br/doc/unidade-organizacional/{unidade}/estrutura"
)
estrutura = estrutura.json()


def orgao(codigo):
  if codigo == 0:
    return {'codigo': 0, 'nome': 'Não informado', 'sigla': 'Não informado'}
  estrutura = requests.get(
      f"http://estruturaorganizacional.dados.gov.br/doc/unidade-organizacional/{codigo}"
  )
  estrutura = estrutura.json()
  estrutura = estrutura['unidade']
  return {
      'SETOR_CODIGO': codigo,
      'SETOR_NOME': estrutura['nome'],
      'SIGLA': estrutura['sigla']
  }


df_setor = pd.DataFrame(columns=[
    'SETOR_CODIGO', 'SETOR_NOME', 'CAMINHO', 'UNIDADE_SIGLA', 'UNIDADE_NOME'
])


#
def pstring(codigo, nome, path, codigo_superior, nome_superior):
  df_setor.loc[len(df_setor)] = [
      codigo, nome, path, codigo_superior, nome_superior
  ]
  return f'''"{codigo}", "{nome}", "{path}", "{codigo_superior}", "{nome_superior}" '''


for e in estrutura['estrutura']['estrutura']:
  o = orgao(e['codigoUnidade'])
  print(
      pstring(o['SETOR_CODIGO'], o['SETOR_NOME'], f"{o['SIGLA']}/UFCA",
              o['SIGLA'], o['SETOR_NOME']))

  if e['estrutura']:
    for ee in e['estrutura']:
      oo = orgao(ee['codigoUnidade'])

      print(
          pstring(oo['SETOR_CODIGO'], oo['SETOR_NOME'],
                  f"{oo['SIGLA']}/{o['SIGLA']}/UFCA", o['SIGLA'],
                  o['SETOR_NOME']))

      if ee['estrutura']:
        for eee in ee['estrutura']:
          ooo = orgao(eee['codigoUnidade'])
          print(
              pstring(ooo['SETOR_CODIGO'], ooo['SETOR_NOME'],
                      f"{ooo['SIGLA']}/{oo['SIGLA']}/{o['SIGLA']}/UFCA",
                      o['SIGLA'], o['SETOR_NOME']))

          if eee['estrutura']:
            for eeee in eee['estrutura']:
              oooo = orgao(eeee['codigoUnidade'])
              print(
                  pstring(
                      oooo['SETOR_CODIGO'], oooo['SETOR_NOME'],
                      f"{oooo['SIGLA']}/{ooo['SIGLA']}/{oo['SIGLA']}/{o['SIGLA']}/UFCA",
                      o['SIGLA'], o['SETOR_NOME']))

st.write(df_setor)
