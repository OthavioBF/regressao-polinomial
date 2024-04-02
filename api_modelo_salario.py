from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib
import pandas as pd

app = FastAPI()

class RequestBody(BaseModel):
  tempo_na_empresa: int
  nivel_na_empresa: int
  
modelo_poly = joblib.load('./modelo_salario.pkl')

@app.post('/predict')
def predict(data: RequestBody):
  input_feature = {
    'tempo_na_empresa': data.tempo_na_empresa, 
    'nivel_na_empresa': data.nivel_na_empresa
  }
  
  pred_df = pd.DataFrame(input_feature, index=[1])
  
  y_pred = modelo_poly.predict(pred_df)[0].astype(float)
  
  return {'salario_em_reais': y_pred.tolist()}
  
  