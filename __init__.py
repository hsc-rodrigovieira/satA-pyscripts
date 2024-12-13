import re
import time
import config
import pandas    as pd
import streamlit as st
from KPI      import KPI
from dbConfig import dbConfig

class App(object):

    def __init__(self):
        self._1_proporcao_partos_vaginais = None
        self._2_proporcao_reinternacoes_30_dias = None
        self._3_taxa_pcr = None
        self._4_taxa_mortalidade = None
        self._5_tempo_medio_internacao = None
        self._6_tempo_medio_emergencia = None
        self._7_tempo_medio_espera_emergencia = None
        self._8_taxa_atb_profilatico = None
        self._9_taxa_infeccao_cirurgia_limpa = None
        self._10_incidencia_ipcs_cvc = None
        self._11_incidencia_itu_cvd = None
        self._12_taxa_profilaxia_tromboembolismo = None
        self._13_incidencia_queda = None
        self._14_evento_sentinela = None

        pass

    def make_dataframe(self, data:dict) -> pd.DataFrame:
        if (not data):
            raise Exception("Collection data not found.")
        else:
            try:
                return pd.json_normalize(data)
            except ValueError as e:
                raise Exception("Unable to load data from the collection: ", e)
            
    def make_result_dict(self, organization_cnes:int, year:int, month:int) -> dict:
        result_dict = {
            "organization_cnes": organization_cnes,
            "year": year,
            "month": month,
            "rkpi1": self._1_proporcao_partos_vaginais,
            **self._2_proporcao_reinternacoes_30_dias,
            "rkpi3": self._3_taxa_pcr,
            **self._4_taxa_mortalidade,
            **self._5_tempo_medio_internacao,
            "rkpi6": self._6_tempo_medio_emergencia,
            **self._7_tempo_medio_espera_emergencia,
            "rkpi8": self._8_taxa_atb_profilatico,
            "rkpi9": self._9_taxa_infeccao_cirurgia_limpa,
            **self._10_incidencia_ipcs_cvc,
            **self._11_incidencia_itu_cvd,
            **self._12_taxa_profilaxia_tromboembolismo,
            "rkpi13": self._13_incidencia_queda,
            "rkpi14": self._14_evento_sentinela
        }
        return result_dict
            
    def calculate(self,df:pd.DataFrame) -> dict:
        self._1_proporcao_partos_vaginais = kpi.kpi1( total_partos_vaginais = df.at[0,'partos_vaginais'],
                                                    total_partos_cesareos = df.at[0,'partos_cesareos'] )
        self._2_proporcao_reinternacoes_30_dias = kpi.kpi2 ( cli_total_reinternacoes_30_dias = df.at[0,'reinternacoes_clinicas'],
                                                        cli_total_saida_mes_anterior = df.at[0,'saidas_clinicas_anterior'],
                                                        cir_total_reinternacoes_30_dias = df.at[0,'reinternacoes_cirurgicas'],
                                                        cir_total_saida_mes_anterior = df.at[0,'saidas_cirurgicas_anterior'] )
        self._3_taxa_pcr = kpi.kpi3( total_pcr = df.at[0,'pcr_eventos'],
                                total_pacientes_dia = df.at[0,'pacientes_dia'] )
        self._4_taxa_mortalidade = kpi.kpi4( cli_neo_precoce_total_obitos = df.at[0,'cli_neo_precoce_obitos'],
                                        cli_neo_precoce_total_saidas = df.at[0,'cli_neo_precoce_saidas'],
                                        cli_neo_tardio_total_obitos = df.at[0,'cli_neo_tardio_obitos'],
                                        cli_neo_tardio_total_saidas = df.at[0,'cli_neo_tardio_saidas'],
                                        cli_pedi_total_obitos = df.at[0,'cli_pedi_obitos'],
                                        cli_pedi_total_saidas = df.at[0,'cli_pedi_saidas'],
                                        cli_ad_total_obitos = df.at[0,'cli_ad_obitos'],
                                        cli_ad_total_saidas = df.at[0,'cli_ad_saidas'],
                                        cli_idoso_total_obitos = df.at[0,'cli_idoso_obitos'],
                                        cli_idoso_total_saidas = df.at[0,'cli_idoso_saidas'],
                                        cir_neo_precoce_total_obitos = df.at[0,'cir_neo_precoce_obitos'],
                                        cir_neo_precoce_total_saidas = df.at[0,'cir_neo_precoce_saidas'],
                                        cir_neo_tardio_total_obitos = df.at[0,'cir_neo_tardio_obitos'],
                                        cir_neo_tardio_total_saidas = df.at[0,'cir_neo_tardio_saidas'],
                                        cir_pedi_total_obitos = df.at[0,'cir_pedi_obitos'],
                                        cir_pedi_total_saidas = df.at[0,'cir_pedi_saidas'],
                                        cir_ad_total_obitos = df.at[0,'cir_ad_obitos'],
                                        cir_ad_total_saidas = df.at[0,'cir_ad_saidas'],
                                        cir_idoso_total_obitos = df.at[0,'cir_idoso_obitos'],
                                        cir_idoso_total_saidas = df.at[0,'cir_idoso_saidas'] )
        self._5_tempo_medio_internacao = kpi.kpi5( cli_pedi_total_pacientes_dia = df.at[0,'cli_pedi_pacientes_dia'],
                                            cli_pedi_total_saidas = df.at[0,'cli_pedi_saidas'],
                                            cli_ad_total_pacientes_dia = df.at[0,'cli_ad_pacientes_dia'],
                                            cli_ad_total_saidas = df.at[0,'cli_ad_saidas'],
                                            cli_idoso_total_pacientes_dia = df.at[0,'cli_idoso_pacientes_dia'],
                                            cli_idoso_total_saidas = df.at[0,'cli_idoso_saidas'],
                                            cir_pedi_total_pacientes_dia = df.at[0,'cir_pedi_pacientes_dia'],
                                            cir_pedi_total_saidas = df.at[0,'cir_pedi_saidas'],
                                            cir_ad_total_pacientes_dia = df.at[0,'cir_ad_pacientes_dia'],
                                            cir_ad_total_saidas = df.at[0,'cir_ad_saidas'],
                                            cir_idoso_total_pacientes_dia = df.at[0,'cir_idoso_pacientes_dia'],
                                            cir_idoso_total_saidas = df.at[0,'cir_idoso_saidas'] )
        self._6_tempo_medio_emergencia = kpi.kpi6( total_tempo_entrada_termino = df.at[0,'total_tempo_permanencia_emergencia_hr'],
                                            total_pacientes_buscaram_atendimento = df.at[0,'total_pacientes_emergencia'] )
        self._7_tempo_medio_espera_emergencia = kpi.kpi7( nvl2_total_tempo_espera = df.at[0,'tempo_total_emergencia_nivel2_min'],
                                                    nvl2_total_pacientes_buscaram_atendimento = df.at[0,'pacientes_emergencia_nivel2'],
                                                    nvl3_total_tempo_espera = df.at[0,'tempo_total_emergencia_nivel3_min'],
                                                    nvl3_total_pacientes_buscaram_atendimento = df.at[0,'pacientes_emergencia_nivel3'] )
        self._8_taxa_atb_profilatico = kpi.kpi8( total_cirurgias_limpas_com_atb = df.at[0,'cirurgias_com_antibiotico'],
                                            total_cirurgias_limpas = df.at[0,'total_cirurgias_limpas'] )
        self._9_taxa_infeccao_cirurgia_limpa = kpi.kpi9( total_isc_30_dias = df.at[0,'total_infeccoes'],
                                                    total_cirurgias_limpas_mes_anterior = df.at[0,'total_cirurgias_limpas_anterior'] )
        self._10_incidencia_ipcs_cvc = kpi.kpi10( ui_neo_total_ipcs = df.at[0,'ui_neo_infec'],
                                            uti_neo_total_ipcs = df.at[0,'uti_neo_infec'],
                                            ui_pedi_total_ipcs = df.at[0,'ui_pedi_infec'],
                                            uti_pedi_total_ipcs = df.at[0,'uti_pedi_infec'],
                                            ui_ad_total_ipcs = df.at[0,'ui_ad_infec'],
                                            uti_ad_total_ipcs = df.at[0,'uti_ad_infec'],
                                            ui_neo_total_cvc_dia = df.at[0,'ui_neo_cvc_dia'],
                                            uti_neo_total_cvc_dia = df.at[0,'uti_neo_cvc_dia'],
                                            ui_pedi_total_cvc_dia = df.at[0,'ui_pedi_cvc_dia'],
                                            uti_pedi_total_cvc_dia = df.at[0,'uti_pedi_cvc_dia'],
                                            ui_ad_total_cvc_dia = df.at[0,'ui_ad_cvc_dia'],
                                            uti_ad_total_cvc_dia = df.at[0,'uti_ad_cvc_dia'] )
        self._11_incidencia_itu_cvd = kpi.kpi11( ui_neo_total_itu = df.at[0,'ui_neo_itu'],
                                            uti_neo_total_itu = df.at[0,'uti_neo_itu'],
                                            ui_pedi_total_itu = df.at[0,'ui_pedi_itu'],
                                            uti_pedi_total_itu = df.at[0,'uti_pedi_itu'],
                                            ui_ad_total_itu = df.at[0,'ui_ad_itu'],
                                            uti_ad_total_itu = df.at[0,'uti_ad_itu'],
                                            ui_neo_total_cvd_dia = df.at[0,'ui_neo_cvd_dia'],
                                            uti_neo_total_cvd_dia = df.at[0,'uti_neo_cvd_dia'],
                                            ui_pedi_total_cvd_dia = df.at[0,'ui_pedi_cvd_dia'],
                                            uti_pedi_total_cvd_dia = df.at[0,'uti_pedi_cvd_dia'],
                                            ui_ad_total_cvd_dia = df.at[0,'ui_ad_cvd_dia'],
                                            uti_ad_total_cvd_dia = df.at[0,'uti_ad_cvd_dia'] )
        self._12_taxa_profilaxia_tromboembolismo = kpi.kpi12( cli_total_pacientes_risco_profilaxia_TEV = df.at[0,'cli_profilaxia'],
                                                        cli_total_pacientes_risco = df.at[0,'cli_total_pacientes'],
                                                        cir_orto_total_pacientes_risco_profilaxia_TEV = df.at[0,'cir_orto_profilaxia'],
                                                        cir_orto_total_pacientes_risco = df.at[0,'cir_orto_total_pacientes'],
                                                        cir_n_orto_total_pacientes_risco_profilaxia_TEV = df.at[0,'cir_nao_orto_profilaxia'],
                                                        cir_n_orto_total_pacientes_risco = df.at[0,'cir_nao_orto_total_pacientes'] )
        self._13_incidencia_queda = kpi.kpi13( total_quedas_dano = df.at[0,'quedas_com_dano'],
                                        total_pacientes_dia = df.at[0,'pacientes_dia'] )
        self._14_evento_sentinela = kpi.kpi14( total_eventos_sentinela = df.at[0,'eventos_sentinela'],
                                        total_pacientes_dia = df.at[0,'pacientes_dia'] )
        result_dict = self.make_result_dict( organization_cnes = int(df.at[0,'organization_cnes']),
                                             year = int(df.at[0,'year']),
                                             month = int(df.at[0,'month']) )
        return result_dict
    
    def get_key_from_value(self,dict:dict,value):
        return next((k for k, v in dict.items() if v == value), None)
    
if __name__=='__main__':
    db = dbConfig()
    kpi = KPI()
    app = App()

    # Configurar estado inicial antes de criar o widget
    if "var_year" not in st.session_state:
        st.session_state.var_year = None
    if "var_month" not in st.session_state:
        st.session_state.var_month = None

    with st.container():    
        st.title("Consolidação de Indicadores")
        st.write(":ringed_planet: Saturn Analytics")

    with st.container():
        st.subheader("Configuração")   
        box_organization = st.selectbox(label="Empresa:",options=db.get_organizations("organizations"),index=None)
        if box_organization:
            organization_cnes = re.search(r"\d+",box_organization).group()
            with st.empty():
                with st.container():          
                    with st.spinner(text="Carregando..."):
                        last_consolidation = db.get_last_consolidation( collection_name="kpi_results",
                                                                        cnes=organization_cnes )
                        if last_consolidation:
                            info = f"Último mês consolidado: {config.MONTH_MASK[last_consolidation[0]['month']]} de {last_consolidation[0]['year']}"
                            st.info(info,icon="ℹ️")
                        else:
                            info = "Nenhuma consolidação foi encontrada para esta empresa."
                            st.warning(info,icon="❕")
        
        col1, col2 = st.columns(2)
        with col1:
            var_year = st.selectbox( placeholder="Selecione o ano",
                                     label="Ano:",
                                     options=config.YEARS,
                                     index=None,
                                     #index=0 if st.session_state.var_year is None else config.YEARS.index(st.session_state.var_year),
                                     key='var_year'
                                    )
        with col2:
            var_month = st.selectbox( placeholder="Selecione o mês",
                                      label="Mês:",
                                      options=config.MONTH_MASK.values(),
                                      index=None,
                                      #index=0 if st.session_state.var_month is None else list(config.MONTH_MASK.values()).index(st.session_state.var_month),
                                      key='var_month'
                                    )        

        if st.button(label="Consolidar", use_container_width=True):            
            st.toast("Consolidando...",icon="⌛")
            metricas = db.get_metrics( collection_name="metrics",
                                       query= { "organization_cnes": int(organization_cnes),
                                                "year": int(var_year),
                                                "month": app.get_key_from_value(config.MONTH_MASK,var_month) } )    
            df = app.make_dataframe( data=metricas )
            result_query = app.calculate( df=df )
            status = db.load_data( collection_name="kpi_results",
                                   query=result_query )              
            if status:
                st.toast(f'Concluído!',icon="✅")
                db.get_last_consolidation.clear()
            else:
                st.toast('Ocorreu um erro!',icon="☠️")