import streamlit as st

def home():
    st.title("Home")

pages = {
    "App":[
        st.Page(home,title="Home",icon=":material/home:"),
        st.Page("pages/consolidacao_indicadores.py", title="Consolidação de Indicadores", icon=":material/add_chart:"),
        st.Page("pages/envio_metricas.py", title="Envio de Métricas", icon=":material/cloud_upload:"), 
    ]
}

st.logo("img/ecg_35dp_E8EAED.svg")
pg = st.navigation(pages)
pg.run()