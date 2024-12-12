import streamlit as st
import time
import re
import config
from dbConfig import dbConfig

db = dbConfig()

with st.container():    
    st.title("Consolidação de Indicadores")
    st.write(":ringed_planet: Saturn Analytics")

with st.container():
    st.subheader("Configuração")   
    box_organization = st.selectbox(label="Empresa:",options=db.get_organizations("organizations"),index=None)
    if box_organization:
        organization_cnes = re.search("\d+",box_organization).group()
        with st.empty():
            with st.container():          
                with st.spinner(text="Carregando..."):
                    last_consolidation = db.get_last_consolidation(collection_name="kpi_results", cnes=organization_cnes)
                    if last_consolidation:
                        info = f"Último mês consolidado: {config.MONTH_MASK[last_consolidation[0]['month']]} de {last_consolidation[0]['year']}"
                        st.info(info,icon="ℹ️")
                    else:
                        info = "Nenhuma consolidação foi encontrada para esta empresa."
                        st.warning(info,icon="❕")
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(label="Ano:",options=config.YEARS,index=None)
    with col2:
        st.selectbox(label="Mês:",options=config.MONTH_MASK.values(),index=None)        

    if st.button(label="Consolidar", use_container_width=True):
        st.toast("Consolidando...",icon="☕")
        time.sleep(.5)
        st.toast('Concluído!',icon="✅")
        time.sleep(.5)
        st.toast('Ocorreu um erro!',icon="❗")