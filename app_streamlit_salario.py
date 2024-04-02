import streamlit as st
import json
import requests

# Titulo da Aplicação
st.title('Modelo de predicao de salario')

# Inputs do usuario
st.write('Quandos meses o profissional esta na empresa')
tempo_na_empresa = st.slider('Meses', min_value=1, max_value=120, value=60, step=1)

st.write('Qual o nivel do profissional na empresa')
nivel_na_empresa = st.slider('Nivel', min_value=1, max_value=10, value=5, step=1)

input_features = {
  'tempo_na_empresa': tempo_na_empresa, 
  'nivel_na_empresa': nivel_na_empresa
}

# Criar um botao e capturar um evento deste botao para disparar a API
if st.button('Estimar Salario'):
  res = requests.post('http://localhost:8000/predict', data=json.dumps(input_features))
  
  res_json = json.loads(res.text)
  
  salario_em_reais = round(res_json['salario_em_reais'], 2)
  st.subheader(f'O salario estimado eh R$ {salario_em_reais}')