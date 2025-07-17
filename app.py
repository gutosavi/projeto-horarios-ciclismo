import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Estimativa de Horários - Prova MTB", layout="centered")

st.title("🚴‍♂️ Estimativa de Horários por Ponto de Apoio")

# Input do usuário
largada = st.time_input("⏰ Horário de Largada", value=datetime.strptime("08:00", "%H:%M").time())

distancias_str = st.text_input("📍 Distâncias dos Pontos de Apoio (km)", value="10, 17, 23, 36, 49, 54")
medias_str = st.text_input("🚴‍♀️ Velocidades Médias (km/h)", value="21, 25, 29")

# Processar entradas
try:
    distancias = [float(x.strip()) for x in distancias_str.split(",")]
    velocidades = [float(x.strip()) for x in medias_str.split(",")]

    # Criar DataFrame
    df = pd.DataFrame({"Ponto": [f"PA{i+1}" for i in range(len(distancias))], "Distância (km)": distancias})

    # Adiciona a largada
    df.loc[-1] = ["Largada", 0]
    df = df.sort_values("Distância (km)").reset_index(drop=True)

    # Função para calcular horários
    def calcular_horarios(dist_km, vel_kmh, largada_time):
        tempo_horas = dist_km / vel_kmh
        tempo_segundos = tempo_horas * 3600
        horario_passagem = (datetime.combine(datetime.today(), largada_time) + timedelta(seconds=tempo_segundos)).time()
        return horario_passagem.strftime("%H:%M")

    # Criar colunas de horário para cada velocidade
    for v in velocidades:
        df[f"{v:.0f} km/h"] = df["Distância (km)"].apply(lambda d: calcular_horarios(d, v, largada))

    st.success("✅ Estimativas geradas com sucesso!")

    st.dataframe(df)

except Exception as e:
    st.error("❌ Erro ao processar os dados. Verifique os campos.")
    st.exception(e)
