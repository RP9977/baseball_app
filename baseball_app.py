import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

datos_jugadores = {
    "Shohei Ohtani": {"AVG": 0.304, "HR": 44, "OBP": 0.412, "ERA": 3.14},
    "Aaron Judge": {"AVG": 0.287, "HR": 37, "OBP": 0.394, "ERA": None},
    "Ronald Acuña Jr.": {"AVG": 0.337, "HR": 41, "OBP": 0.416, "ERA": None},
    "Mike Trout": {"AVG": 0.290, "HR": 40, "OBP": 0.410, "ERA": None},
    "Mookie Betts": {"AVG": 0.311, "HR": 35, "OBP": 0.410, "ERA": None},
    "Freddie Freeman": {"AVG": 0.325, "HR": 30, "OBP": 0.405, "ERA": None},
    "Juan Soto": {"AVG": 0.290, "HR": 33, "OBP": 0.420, "ERA": None}
}

def generar_analisis(jugador):
    """Genera un análisis del rendimiento del jugador usando OpenAI."""
    estadisticas = datos_jugadores.get(jugador)
    
    if not estadisticas:
        return f"No se encontraron estadísticas para {jugador}."
    
    prompt = f"""
    Analiza el rendimiento de {jugador} en base a las siguientes estadísticas:
    AVG: {estadisticas['AVG']}
    HR: {estadisticas['HR']}
    OBP: {estadisticas['OBP']}
    ERA: {estadisticas['ERA']}
    
    Proporciona un breve análisis destacando fortalezas y oportunidades de mejora.
    """
    
    respuesta = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Eres un analista de béisbol experto."},
        {"role": "user", "content": prompt}
        ]
    )
    
    return respuesta["choices"][0]["message"]["content"]

st.title("Club House - Análisis Inteligente de Jugadores")
st.write("Ingresa el nombre de un jugador y obtén un análisis de su rendimiento basado en estadísticas.")

jugador_seleccionado = st.selectbox("Selecciona un jugador", list(datos_jugadores.keys()))

if st.button("Generar Análisis"):
    resultado = generar_analisis(jugador_seleccionado)
    st.write(resultado)
