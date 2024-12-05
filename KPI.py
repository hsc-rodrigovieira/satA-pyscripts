import pandas as pd

class KPI(object):

    def __init__ ( self ):
        """
        Construtor da classe.

        Não retorna nenhum valor.
        """
        pass

    def calcular( self, metrics:pd.DataFrame ) -> pd.DataFrame:

        if (metrics):
        # 1. Proporção de partos vaginais   
            kpi1 = ( metrics.partos_vaginais / (metrics.partos_vaginais + metrics.partos_cesareos) )[0] *100

        # 2. Proporção de reinternações em até 30 dias da saída hospitalar
            kpi2_cli = ( metrics.reinternacoes_clinicas / metrics.saidas_clinicas_anterior )[0] *100
            kpi2_cir = ( metrics.reinternacoes_cirurgicas / metrics.saidas_cirurgicas_anterior )[0] *100
            kpi2 = ((metrics.reinternacoes_clinicas+metrics.reinternacoes_cirurgicas) / (metrics.saidas_clinicas_anterior+metrics.saidas_cirurgicas_anterior))[0]* 100

        # 3. Taxa de parada cardiorrespiratória em unidade de internação
            kpi3 = ( metrics.pcr_eventos / metrics.pacientes_dia )[0] *1000

        # 4. Taxa de mortalidade institucional
            kpi4_cli_neo_precoce = ( metrics.cli_neo_precoce_obitos / metrics.cli_neo_precoce_saidas )[0] *100
            kpi4_cli_neo_tardio  = ( metrics.cli_neo_tardio_obitos  / metrics.cli_neo_tardio_saidas  )[0] *100
            kpi4_cli_pedi        = ( metrics.cli_pedi_obitos        / metrics.cli_pedi_saidas        )[0] *100
            kpi4_cli_adulto      = ( metrics.cli_ad_obitos          / metrics.cli_ad_saidas          )[0] *100
            kpi4_cli_idoso       = ( metrics.cli_idoso_obitos       / metrics.cli_idoso_saidas       )[0] *100

            kpi4_cir_neo_precoce = ( metrics.cir_neo_precoce_obitos / metrics.cir_neo_precoce_saidas )[0] *100
            kpi4_cir_neo_tardio  = ( metrics.cir_neo_tardio_obitos  / metrics.cir_neo_tardio_saidas  )[0] *100
            kpi4_cir_pedi        = ( metrics.cir_pedi_obitos        / metrics.cir_pedi_saidas        )[0] *100
            kpi4_cir_adulto      = ( metrics.cir_ad_obitos          / metrics.cir_ad_saidas          )[0] *100
            kpi4_cir_idoso       = ( metrics.cir_idoso_obitos       / metrics.cir_idoso_saidas       )[0] *100

            kpi4_cli = (
                ( metrics.cli_neo_precoce_obitos+
                  metrics.cli_neo_tardio_obitos+
                  metrics.cli_pedi_obitos+
                  metrics.cli_ad_obitos+
                  metrics.cli_idoso_obitos ) / 
                ( metrics.cli_neo_precoce_saidas+
                  metrics.cli_neo_tardio_saidas+
                  metrics.cli_pedi_saidas+
                  metrics.cli_ad_saidas+
                  metrics.cli_idoso_saidas )
            )[0] *100

            kpi4_cir = (
                ( metrics.cir_neo_precoce_obitos+
                  metrics.cir_neo_tardio_obitos+
                  metrics.cir_pedi_obitos+
                  metrics.cir_ad_obitos+
                  metrics.cir_idoso_obitos ) / 
                ( metrics.cir_neo_precoce_saidas+
                  metrics.cir_neo_tardio_saidas+
                  metrics.cir_pedi_saidas+
                  metrics.cir_ad_saidas+
                  metrics.cir_idoso_saidas )
            )[0] *100

            kpi4_neo_precoce = (
                ( metrics.cli_neo_precoce_obitos+metrics.cir_neo_precoce_obitos ) / 
                ( metrics.cli_neo_precoce_saidas+metrics.cir_neo_precoce_saidas )
            )[0] *100

            kpi4_neo_tardio = (
                ( metrics.cli_neo_tardio_obitos+metrics.cir_neo_tardio_obitos ) / 
                ( metrics.cli_neo_tardio_saidas+metrics.cir_neo_tardio_saidas )
            )[0] *100

            kpi4_pedi = (
                ( metrics.cli_pedi_obitos+metrics.cir_pedi_obitos ) / 
                ( metrics.cli_pedi_saidas+metrics.cir_pedi_saidas )
            )[0] *100

            kpi4_ad = (
                ( metrics.cli_ad_obitos+metrics.cir_ad_obitos ) / 
                ( metrics.cli_ad_saidas+metrics.cir_ad_saidas )
            )[0] *100

            kpi4_idoso = (
                ( metrics.cli_idoso_obitos+metrics.cir_idoso_obitos ) / 
                ( metrics.cli_idoso_saidas+metrics.cir_idoso_saidas )
            )[0] *100

            kpi4_cir = (
                ( metrics.cir_neo_precoce_obitos+
                  metrics.cir_neo_tardio_obitos+
                  metrics.cir_pedi_obitos+
                  metrics.cir_ad_obitos+
                  metrics.cir_idoso_obitos ) / 
                ( metrics.cir_neo_precoce_saidas+
                  metrics.cir_neo_tardio_saidas+
                  metrics.cir_pedi_saidas+
                  metrics.cir_ad_saidas+
                  metrics.cir_idoso_saidas )
            )[0] *100    

            kpi4 = (
                metrics.cli_neo_precoce_obitos+
                metrics.cli_neo_tardio_obitos+
                metrics.cli_pedi_obitos+
                metrics.cli_ad_obitos+
                metrics.cli_idoso_obitos+
                metrics.cir_neo_precoce_obitos+
                metrics.cir_neo_tardio_obitos+
                metrics.cir_pedi_obitos+
                metrics.cir_ad_obitos+
                metrics.cir_idoso_obitos
            ) / (
                metrics.cli_neo_precoce_saidas+
                metrics.cli_neo_tardio_saidas+
                metrics.cli_pedi_saidas+
                metrics.cli_ad_saidas+
                metrics.cli_idoso_saidas+
                metrics.cir_neo_precoce_saidas+
                metrics.cir_neo_tardio_saidas+
                metrics.cir_pedi_saidas+
                metrics.cir_ad_saidas+
                metrics.cir_idoso_saidas
            )[0] *100
        
        # 5. Tempo médio de internação
            kpi5_cli_pedi   = ( metrics.cli_pedi_pacientes_dia  / metrics.cli_pedi_saidas)[0]
            kpi5_cli_adulto = ( metrics.cli_ad_pacientes_dia    / metrics.cli_ad_saidas)[0]
            kpi5_cli_idoso  = ( metrics.cli_idoso_pacientes_dia / metrics.cli_idoso_saidas)[0]
            kpi5_cir_pedi   = ( metrics.cir_pedi_pacientes_dia  / metrics.cir_pedi_saidas)[0]
            kpi5_cir_adulto = ( metrics.cir_ad_pacientes_dia    / metrics.cir_ad_saidas)[0]
            kpi5_cir_idoso  = ( metrics.cir_idoso_pacientes_dia / metrics.cir_idoso_saidas)[0]
            kpi5_cli = ( ( metrics.cli_pedi_pacientes_dia+metrics.cli_ad_pacientes_dia+metrics.cli_idoso_pacientes_dia ) / 
                         ( metrics.cli_pedi_saidas+metrics.cli_ad_saidas+metrics.cli_idoso_saidas ) )[0]
            kpi5_cir = ( ( metrics.cir_pedi_pacientes_dia+metrics.cir_ad_pacientes_dia+metrics.cir_idoso_pacientes_dia ) / 
                         ( metrics.cir_pedi_saidas+metrics.cir_ad_saidas+metrics.cir_idoso_saidas ) )[0]
            kpi5_pedi = ( ( metrics.cli_pedi_pacientes_dia+metrics.cir_pedi_pacientes_dia ) / 
                          ( metrics.cli_pedi_saidas+metrics.cir_pedi_saidas ) )[0] *100
            kpi5_ad = ( ( metrics.cli_ad_pacientes_dia+metrics.cir_ad_pacientes_dia ) / 
                        ( metrics.cli_ad_saidas+metrics.cir_ad_saidas ) )[0]
            kpi5_idoso = ( ( metrics.cli_idoso_pacientes_dia+metrics.cir_idoso_pacientes_dia ) / 
                           ( metrics.cli_idoso_saidas+metrics.cir_idoso_saidas ) )[0]
            kpi5 = ( metrics.cli_pedi_pacientes_dia+metrics.cli_ad_pacientes_dia+metrics.cli_idoso_pacientes_dia+
                     metrics.cir_pedi_pacientes_dia+metrics.cir_ad_pacientes_dia+metrics.cir_idoso_pacientes_dia ) / (
                     metrics.cli_pedi_saidas+metrics.cli_ad_saidas+metrics.cli_idoso_saidas+
                     metrics.cir_pedi_saidas+metrics.cir_ad_saidas+metrics.cir_idoso_saidas )[0]

        # 6. Tempo médio de permanência na emergência
            kpi6 = ( metrics.total_tempo_permanencia_emergencia_hr / metrics.total_pacientes_emergencia )[0]

        # 7. Tempo médio de espera na emergência para primeiro atendimento
            kpi7_nvl2 = ( metrics.tempo_total_emergencia_nivel2_min / metrics.pacientes_emergencia_nivel2 )[0]
            kpi7_nvl3 = ( metrics.tempo_total_emergencia_nivel3_min / metrics.pacientes_emergencia_nivel3 )[0]
            kpi7 = ( ( metrics.tempo_total_emergencia_nivel2_min+metrics.tempo_total_emergencia_nivel3_min ) /
                     ( metrics.pacientes_emergencia_nivel2+metrics.pacientes_emergencia_nivel3 ) )[0]
            
        # 8. Taxa de início de antibiótico intravenoso profilático
            kpi8 = ( metrics.cirurgias_com_antibiotico / metrics.total_cirurgias_limpas )[0] *100
            
        # 9. Taxa de infecção de sítio cirúrgico em cirurgia limpa
            kpi9 = ( metrics.total_infeccoes / metrics.total_cirurgias_limpas )[0] *100
            
        # 10. Densidade de incidência de infecção primária de corrente sanguínea (IPCS)
        # em pacientes em uso de cateter venoso central (CVC)
            kpi10_neo = ( ( metrics.unid_int_neo_precoce_infec + metrics.unid_int_neo_tardio_infec ) / 
                          ( metrics.unid_int_neo_precoce_cvc_dia + metrics.unid_int_neo_tardio_cvc_dia ) )[0] *1000
            kpi10_pedi = ( metrics.unid_int_pedi_infec / metrics.unid_int_pedi_cvc_dia )[0] *1000
            kpi10_ad = ( ( metrics.unid_int_ad_infec + metrics.unid_int_idoso_infec ) /
                         ( metrics.unid_int_ad_cvc_dia + metrics.unid_int_idoso_cvc_dia ) )[0] *1000
            kpi10_neo_uti = ( ( metrics.uti_neo_precoce_infec + metrics.uti_neo_tardio_infec ) / 
                              ( metrics.uti_neo_precoce_cvc_dia + metrics.uti_neo_tardio_cvc_dia ) )[0] *1000
            kpi10_pedi_uti = ( metrics.uti_pedi_infec / metrics.uti_pedi_cvc_dia )[0] *1000
            kpi10_ad_uti = ( ( metrics.uti_ad_infec + metrics.uti_idoso_infec ) / 
                             ( metrics.uti_ad_cvc_dia + metrics.uti_idoso_cvc_dia ) )[0] *1000
            kpi10_unid_int = (
                (   metrics.unid_int_neo_precoce_infec+
                    metrics.unid_int_neo_tardio_infec+
                    metrics.unid_int_pedi_infec+
                    metrics.unid_int_ad_infec+
                    metrics.unid_int_idoso_infec
                ) /                 
                (   metrics.unid_int_neo_precoce_cvc_dia+
                    metrics.unid_int_neo_tardio_cvc_dia+
                    metrics.unid_int_pedi_cvc_dia+
                    metrics.unid_int_ad_cvc_dia+
                    metrics.unid_int_idoso_cvc_dia
                )
            )[0] *1000
            kpi10_uti = (
                (   metrics.uti_neo_precoce_infec+
                    metrics.uti_neo_tardio_infec+
                    metrics.uti_pedi_infec+
                    metrics.uti_ad_infec+
                    metrics.uti_idoso_infec
                ) /                 
                (   metrics.uti_neo_precoce_cvc_dia+
                    metrics.uti_neo_tardio_cvc_dia+
                    metrics.uti_pedi_cvc_dia+
                    metrics.uti_ad_cvc_dia+
                    metrics.uti_idoso_cvc_dia
                )
            )[0] *1000      
            kpi10_neo = (
                (   metrics.uti_neo_precoce_infec+
                    metrics.uti_neo_tardio_infec+
                    metrics.unid_int_neo_precoce_infec+
                    metrics.unid_int_neo_tardio_infec
                ) /                 
                (   metrics.uti_neo_precoce_cvc_dia+
                    metrics.uti_neo_tardio_cvc_dia+
                    metrics.unid_int_neo_precoce_cvc_dia+
                    metrics.unid_int_neo_tardio_cvc_dia
                )
            )[0] *1000
            kpi10_pedi = (
                (   metrics.uti_pedi_infec+
                    metrics.unid_int_pedi_infec
                ) /                 
                (   metrics.uti_pedi_cvc_dia+
                    metrics.unid_int_pedi_cvc_dia
                )
            )[0] *1000            
            kpi10_ad = (
                (   metrics.uti_ad_infec+
                    metrics.uti_idoso_infec+
                    metrics.unid_int_ad_infec+
                    metrics.unid_int_idoso_infec
                ) /                 
                (   metrics.uti_ad_cvc_dia+
                    metrics.uti_idoso_cvc_dia+
                    metrics.unid_int_ad_cvc_dia+
                    metrics.unid_int_idoso_cvc_dia
                )
            )[0] *1000

        # 11. Densidade de incidência de infecção do trato urinário (ITU) associada a um
        # cateter vesical de demora (CVD)
            kpi11_neo = ( ( metrics.unid_int_neo_precoce_itu + metrics.unid_int_neo_tardio_itu ) / 
                          ( metrics.unid_int_neo_precoce_cvd_dia + metrics.unid_int_neo_tardio_cvd_dia ) )[0] *1000
            kpi11_pedi = ( metrics.unid_int_pedi_itu / metrics.unid_int_pedi_cvd_dia )[0] *1000
            kpi11_ad = ( ( metrics.unid_int_ad_itu + metrics.unid_int_idoso_itu ) /
                         ( metrics.unid_int_ad_cvd_dia + metrics.unid_int_idoso_cvd_dia ) )[0] *1000
            kpi11_neo_uti = ( ( metrics.uti_neo_precoce_itu + metrics.uti_neo_tardio_itu ) / 
                              ( metrics.uti_neo_precoce_cvd_dia + metrics.uti_neo_tardio_cvd_dia ) )[0] *1000
            kpi11_pedi_uti = ( metrics.uti_pedi_itu / metrics.uti_pedi_cvd_dia )[0] *1000
            kpi11_ad_uti = ( ( metrics.uti_ad_itu + metrics.uti_idoso_itu ) / 
                             ( metrics.uti_ad_cvd_dia + metrics.uti_idoso_cvd_dia ) )[0] *1000
            kpi11_unid_int = (
                (   metrics.unid_int_neo_precoce_itu+
                    metrics.unid_int_neo_tardio_itu+
                    metrics.unid_int_pedi_itu+
                    metrics.unid_int_ad_itu+
                    metrics.unid_int_idoso_itu
                ) /                 
                (   metrics.unid_int_neo_precoce_cvd_dia+
                    metrics.unid_int_neo_tardio_cvd_dia+
                    metrics.unid_int_pedi_cvd_dia+
                    metrics.unid_int_ad_cvd_dia+
                    metrics.unid_int_idoso_cvd_dia
                )
            )[0] *1000
            kpi11_uti = (
                (   metrics.uti_neo_precoce_itu+
                    metrics.uti_neo_tardio_itu+
                    metrics.uti_pedi_itu+
                    metrics.uti_ad_itu+
                    metrics.uti_idoso_itu
                ) /                 
                (   metrics.uti_neo_precoce_cvd_dia+
                    metrics.uti_neo_tardio_cvd_dia+
                    metrics.uti_pedi_cvd_dia+
                    metrics.uti_ad_cvd_dia+
                    metrics.uti_idoso_cvd_dia
                )
            )[0] *1000      
            kpi11_neo = (
                (   metrics.uti_neo_precoce_itu+
                    metrics.uti_neo_tardio_itu+
                    metrics.unid_int_neo_precoce_itu+
                    metrics.unid_int_neo_tardio_itu
                ) /                 
                (   metrics.uti_neo_precoce_cvd_dia+
                    metrics.uti_neo_tardio_cvd_dia+
                    metrics.unid_int_neo_precoce_cvd_dia+
                    metrics.unid_int_neo_tardio_cvd_dia
                )
            )[0] *1000
            kpi11_pedi = (
                (   metrics.uti_pedi_itu+
                    metrics.unid_int_pedi_itu
                ) /                 
                (   metrics.uti_pedi_cvd_dia+
                    metrics.unid_int_pedi_cvd_dia
                )
            )[0] *1000            
            kpi11_ad = (
                (   metrics.uti_ad_itu+
                    metrics.uti_idoso_itu+
                    metrics.unid_int_ad_itu+
                    metrics.unid_int_idoso_itu
                ) /                 
                (   metrics.uti_ad_cvd_dia+
                    metrics.uti_idoso_cvd_dia+
                    metrics.unid_int_ad_cvd_dia+
                    metrics.unid_int_idoso_cvd_dia
                )
            )[0] *1000        
        
        # 12. Taxa de profilaxia de tromboembolismo venoso
            kpi12_cli          = ( metrics.cli_profilaxia          / metrics.cli_total_pacientes )[0] *100
            kpi12_cir_orto     = ( metrics.cir_orto_profilaxia     / metrics.cir_orto_total_pacientes )[0] *100
            kpi12_cir_nao_orto = ( metrics.cir_nao_orto_profilaxia / metrics.cir_nao_orto_total_pacientes )[0] *100
            kpi12 = ( ( metrics.cli_profilaxia+metrics.cir_orto_profilaxia+metrics.cir_nao_orto_profilaxia ) /
                      ( metrics.cli_total_pacientes+metrics.cir_orto_total_pacientes+metrics.cir_nao_orto_total_pacientes )
                    )[0] *100

        # 13. Densidade de incidência de queda resultando em lesão em paciente
            kpi13 = ( metrics.quedas_com_dano / 
                      ( metrics.cli_neo_precoce_pacientes_dia+
                        metrics.cli_neo_tardio_pacientes_dia+
                        metrics.cli_pedi_pacientes_dia+
                        metrics.cli_ad_pacientes_dia+
                        metrics.cli_idoso_pacientes_dia+
                        metrics.cir_neo_precoce_pacientes_dia+
                        metrics.cir_neo_tardio_pacientes_dia+
                        metrics.cir_pedi_pacientes_dia+
                        metrics.cir_ad_pacientes_dia+
                        metrics.cir_idoso_pacientes_dia )
                      )[0] *1000
        
        # 14. Evento sentinela
            kpi14 = ( metrics.eventos_sentinela / 
                      ( metrics.cli_neo_precoce_pacientes_dia+
                        metrics.cli_neo_tardio_pacientes_dia+
                        metrics.cli_pedi_pacientes_dia+
                        metrics.cli_ad_pacientes_dia+
                        metrics.cli_idoso_pacientes_dia+
                        metrics.cir_neo_precoce_pacientes_dia+
                        metrics.cir_neo_tardio_pacientes_dia+
                        metrics.cir_pedi_pacientes_dia+
                        metrics.cir_ad_pacientes_dia+
                        metrics.cir_idoso_pacientes_dia )
                    )[0] *1000
        else:
            raise Exception("Dados em branco")
    
    
        
    return 
        
