import streamlit as st
import config
from src.App import App
from src.dbConfig import dbConfig

app = App()
db = dbConfig()

st.title("Envio de métricas")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    validacao, dados = app.valida_arquivo(arquivo=uploaded_file)
    if validacao:
        if st.button("Enviar dados",icon=config.ICON_PAGE_ENVIO_METRICAS,use_container_width=True):
            st.toast("Fazendo upload do arquivo...",icon="⌛")            
            ack, var = db.upload_arquivo( dataframe=dados,
                                          collection_name="metrics" )
            if ack:
                st.toast(f'Upload concluído com sucesso! {var} registros incluídos',icon="✅")
            else:
                st.toast(f'Ocorreu um erro! {var}',icon="☠️")
    