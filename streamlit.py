import streamlit as st
import time
from dbConfig      import dbConfig

db = dbConfig()


with st.container():    
    st.title("Consolidação de Indicadores")
    st.write(":ringed_planet: Saturn Analytics")

with st.container():
    st.subheader("Configuração")   
    #if st.selectbox(label="Empresa:",options=["Hospital A", "Hospital B"],index=None):
    if st.selectbox(label="Empresa:",options=db.get_organizations("organizations"),index=None):
        st.info("Último mês consolidado: Novembro de 2024")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(label="Ano:",options=(2023,2024),index=None)
    with col2:
        a = st.selectbox(label="Mês:",options=("Jan", "Fev", "Mar", "Abr", "Maio", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"),index=None)
        st.write(a)

    if st.button(label="Consolidar", help="Executar a consolidação dos indicadores", use_container_width=True):
        st.toast("Consolidando",icon="☕")
        time.sleep(.5)
        st.toast('Concluído!',icon="✅")
        time.sleep(.5)
        st.toast('Ocorreu um erro!',icon="❗")