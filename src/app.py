import streamlit as st
import pandas as pd
import numpy as np
import joblib

model_series = joblib.load('./models/model_patient_renal.pkl')
scaler = joblib.load('./models/scaler_patient_renal.pkl')

st.title("🩺 Você é paciente renal crônico?")
st.markdown("Preencha os dados abaixo para descobrir a probabilidade de ter doença renal crônica.")

col1, col2 = st.columns(2)

with col1:
    idade = st.slider("Idade (anos)", 0, 100, 30)
    diabetes = st.radio("Você é diabético?", ["Sim", "Não"], index=1)
    creatinina = st.slider("Creatinina sanguínea (mg/dL)", 0.0, 10.0, 1.0, 0.1)
    taxa_filtracao = st.slider("Taxa de Filtração Glomerular (mL/min)", 0.0, 130.0, 90.0, 0.1)

with col2:
    hipertensao = st.radio("Você é hipertenso?", ["Sim", "Não"], index=1)
    ureia = st.slider("Ureia sanguínea (mg/dL)", 0.0, 100.0, 40.0, 0.1)
    producao_urina = st.slider("Produção de urina (mL/dia)", 0.0, 2000.0, 1000.0, 1.0)

diabetes_num = 1 if diabetes == "Sim" else 0
hipertensao_num = 1 if hipertensao == "Sim" else 0

if st.button("Verificar risco"):
    input_data = pd.DataFrame({
        'idade': [idade],
        'creatinina_sanguinea': [creatinina],
        'ureia_sanguinea': [ureia],
        'diabetes': [diabetes_num],
        'hipertensao': [hipertensao_num],
        'taxa_filtracao_glomerular': [taxa_filtracao],
        'producao_urina': [producao_urina]
    })

    input_data_scaled = scaler.transform(input_data)
    print(input_data.columns)

    pred = model_series.predict(input_data_scaled)[0]
    prob = model_series.predict_proba(input_data_scaled)[0][1]

    if pred == 1:
        st.error(f"⚠️ Resultado: Alta probabilidade de doença renal crônica ({prob:.1%} de chance). Procure um médico.")
    else:
        st.success(f"✅ Resultado: Baixa probabilidade de doença renal crônica ({prob:.1%} de chance). Continue cuidando da sua saúde!")

st.markdown("---")
st.caption("Modelo baseado em dados clínicos para auxiliar na triagem de pacientes com doença renal crônica.")
