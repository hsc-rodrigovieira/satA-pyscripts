import pandas as pd
from KPI           import KPI
from dbConfig      import dbConfig
from bson.objectid import ObjectId

def make_dataframe(data:dict) -> pd.DataFrame:
    if (not data):
        raise Exception("Collection data not found.")
    else:
        try:
            return pd.json_normalize(data)
        except ValueError as e:
            raise Exception("Unable to load data from the collection: ", e)

if __name__=='__main__':

    db = dbConfig()
    kpi = KPI()

    metricas = db.get_data( collection_name="metrics",
                            query= { "organization_id": ObjectId("6745d7873f4e39e161319575"),
                                     "year": 2023,
                                     "month": 1 } )
    
    df = make_dataframe( data=metricas )

    _1_proporcao_partos_vaginais = kpi.kpi1( total_partos_vaginais = df.at[0,'partos_vaginais'],
                                             total_partos_cesareos = df.at[0,'partos_cesareos'] )
    _2_proporcao_reinternacoes_30_dias = kpi.kpi2 ( cli_total_reinternacoes_ate_30_dias = df.at[0,'reinternacoes_clinicas'],
                                                    cli_total_saida_mes_anterior = df.at[0,'saidas_clinicas_anterior'],
                                                    cir_total_reinternacoes_ate_30_dias = df.at[0,'reinternacoes_cirurgicas'],
                                                    cir_total_saida_mes_anterior = df.at[0,'saidas_cirurgicas_anterior'] )
    _3_taxa_pcr = kpi.kpi3( total_pcr = df.at[0,'pcr_eventos'],
                            total_pacientes_dia = df.at[0,'pacientes_dia'] )
    _4_taxa_mortalidade = kpi.kpi4( cli_neo_precoce_total_obitos = df.at[0,'cli_neo_precoce_obitos'],
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


    
    print('hello world')