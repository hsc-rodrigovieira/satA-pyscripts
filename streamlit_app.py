import streamlit as st
import config

def home():
    st.title("Home")
    st.image(config.PATH_HOME_IMG, width=300)

pages = {
    "App":[
        st.Page(home,title="Home",icon=config.ICON_PAGE_HOME),
        st.Page("pages/consolidacao_indicadores.py", title="Consolidação de Indicadores", icon=config.ICON_PAGE_CONSOLIDACAO),
        st.Page("pages/envio_metricas.py", title="Envio de Métricas", icon=config.ICON_PAGE_ENVIO_METRICAS), 
    ]
}

st.logo(config.PATH_LOGO)
pg = st.navigation(pages)
pg.run()