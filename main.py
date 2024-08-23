import streamlit as st
import os

from stream_generation import stream_answer
from transcribe import transcribe_audio


# === Configuração de Página e Aplicação ===
st.set_page_config(
    page_title="Transcrição de Áudio para Reunião",
    layout="wide"
)

SAVE_DIR = "uploaded_files"
os.makedirs(SAVE_DIR, exist_ok=True)


# === Elementos de Página === 
st.title("Transcrição de Áudio para Ata de Reunião")
st.markdown("_Faça o upload de um arquivo para fazer a transcrição._")

upload = st.file_uploader(label = "Insira um árquivo de áudio (mp3, mkv, wav).", type=["mp3", "mkv", "wav"])

if upload is not None:
    
    # Salvando Arquivo...
    file_path = os.path.join(SAVE_DIR, upload.name)

    with open(file_path, "wb") as file:
        file.write(upload.getbuffer())

    st.success(f"Arquivo {upload.name} recebido.")


    # Tela de Escolha
    st.write("")
    st.write("")
    st.divider()
    
    st.subheader("Transcrição de Áudio")
    model_type = st.selectbox("Escolha o modelo que deseja utilizar.", options=["tiny", "base", "small", "medium", "large"], index = 1)
    
    if st.button("Transcrever"):
        transcription = transcribe_audio(file_path, model_type)

        st.write_stream(stream_answer(transcription))
