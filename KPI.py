import pandas as pd
from typing import Callable

class KPI(object):

    def __init__ ( self ):
        pass

    def validar_kwargs(kwargs, chaves_obrigatorias):
        # Validar se kwargs está vazio
        if not kwargs:
            raise ValueError("Os argumentos kwargs não podem estar vazios.")
        
        # Validar se todas as chaves obrigatórias estão presentes
        for chave in chaves_obrigatorias:
            if chave not in kwargs:
                raise KeyError(f"A chave obrigatória '{chave}' está ausente.")
        
        # Validar se os valores das chaves obrigatórias não são nulos
        for chave in chaves_obrigatorias:
            if kwargs[chave] is None:
                raise ValueError(f"O valor da chave '{chave}' não pode ser nulo.")
        
        # Retornar True se tudo estiver válido
        return True
        
    def kpi_taxa(self, numerador,denominador):
        return (numerador/denominador)[0] *100

    def kpi_tempo_medio(self, numerador,denominador):
        return (numerador/denominador)[0]

    def kpi_densidade(self, numerador,denominador):
        return (numerador/denominador)[0] *1000
    
    def kpi1(self, **kwargs) -> int:
        # 1. Proporção de partos vaginais 
        chaves_obrigatorias = ['total_partos_vaginais','total_partos_cesareos']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            # Calcular o KPI
            total_partos = kwargs['total_partos_vaginais'] + kwargs['total_partos_cesareos']            
            return self.kpi_taxa( numerador = kwargs['total_partos_vaginais'],
                                  denominador = total_partos )
        else:
            return None
    
    def kpi2(self, **kwargs) -> tuple:
        # 2. Proporção de reinternações em até 30 dias da saída hospitalar
        chaves_obrigatorias = ['cli_total_reinternacoes_ate_30_dias',
                               'cli_total_saida_mes_anterior',
                               'cir_total_reinternacoes_ate_30_dias',
                               'cir_total_saida_mes_anterior']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):                
            total_reinternacoes_ate_30_dias = kwargs['cli_total_reinternacoes_30_dias']+kwargs['cir_total_reinternacoes_30_dias']
            total_saidas_mes_anterior = kwargs['cli_total_saida_mes_anterior']+kwargs['cir_total_saida_mes_anterior']
            clinico = self.kpi_taxa( numerador = kwargs['cli_total_reinternacoes_30_dias'],
                                     denominador = kwargs['cli_total_saida_mes_anterior'])
            cirurgico = self.kpi_taxa( numerador = kwargs['cir_total_reinternacoes_30_dias'],
                                       denominador = kwargs['cir_total_saida_mes_anterior'])
            geral = self.kpi_taxa( numerador = total_reinternacoes_ate_30_dias,
                                   denominador = total_saidas_mes_anterior )
            return clinico, cirurgico, geral
        else:
            return None
    
    def kpi3(self, **kwargs) -> int:
        # 3. Taxa de parada cardiorrespiratória em unidade de internação
        chaves_obrigatorias = ['total_pcr','total_pacientes_dia']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):
            # Calcular o KPI        
            return self.kpi_densidade( numerador = kwargs['total_pcr'],
                                       denominador = kwargs['total_pacientes_dia'] )
        else:
            return None        

    def kpi4(self, **kwargs) -> int:
        # 4. Taxa de mortalidade institucional
        chaves_obrigatorias = [
            'cli_neo_precoce_obitos','cli_neo_precoce_saidas',
            'cli_neo_tardio_obitos','cli_neo_tardio_saidas',
            'cli_pedi_obitos','cli_pedi_saidas',
            'cli_ad_obitos','cli_ad_saidas',
            'cli_idoso_obitos','cli_idoso_saidas',
            'cir_neo_precoce_obitos','cir_neo_precoce_saidas',
            'cir_neo_tardio_obitos','cir_neo_tardio_saidas',
            'cir_pedi_obitos','cir_pedi_saidas',
            'cir_ad_obitos','cir_ad_saidas',
            'cir_idoso_obitos','cir_idoso_saidas'
        ]

        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):
            # Calcular o KPI        
            cli_total_obitos = kwargs['cli_neo_precoce_total_obitos']+kwargs['cli_neo_tardio_total_obitos']+kwargs['cli_pedi_total_obitos']+kwargs['cli_ad_total_obitos']+kwargs['cli_idoso_total_obitos']
            cir_total_obitos = kwargs['cir_neo_precoce_total_obitos']+kwargs['cir_neo_tardio_total_obitos']+kwargs['cir_pedi_total_obitos']+kwargs['cir_ad_total_obitos']+kwargs['cir_idoso_total_obitos']
            cli_total_saidas = kwargs['cli_neo_precoce_total_saidas']+kwargs['cli_neo_tardio_total_saidas']+kwargs['cli_pedi_total_saidas']+kwargs['cli_ad_total_saidas']+kwargs['cli_idoso_total_saidas']
            cir_total_saidas = kwargs['cir_neo_precoce_total_saidas']+kwargs['cir_neo_tardio_total_saidas']+kwargs['cir_pedi_total_saidas']+kwargs['cir_ad_total_saidas']+kwargs['cir_idoso_total_saidas']
            
            neo_precoce_total_obitos = kwargs['cli_neo_precoce_total_obitos']+kwargs['cir_neo_precoce_total_obitos']
            neo_tardio_total_obitos = kwargs['cli_neo_tardio_total_obitos']+kwargs['cir_neo_tardio_total_obitos']


            ####

            cli_pedi = self.kpi_tempo_medio( numerador = kwargs['cli_pedi_total_pacientes_dia'],
                                            denominador = kwargs['cli_pedi_total_saidas'])
            cli_ad = self.kpi_tempo_medio( numerador = kwargs['cli_ad_total_pacientes_dia'],
                                           denominador = kwargs['cli_ad_total_saidas'])
            cli_idoso = self.kpi_tempo_medio( numerador = kwargs['cli_idoso_total_pacientes_dia'],
                                              denominador = kwargs['cli_idoso_total_saidas'])
            cir_pedi = self.kpi_tempo_medio( numerador = kwargs['cir_pedi_total_pacientes_dia'],
                                             denominador = kwargs['cir_pedi_total_saidas'])
            cir_ad = self.kpi_tempo_medio( numerador = kwargs['cir_ad_total_pacientes_dia'],
                                           denominador = kwargs['cir_ad_total_saidas'])
            cir_idoso = self.kpi_tempo_medio( numerador = kwargs['cir_idoso_total_pacientes_dia'],
                                              denominador = kwargs['cir_idoso_total_saidas'])
            clinico = self.kpi_tempo_medio( numerador = cli_total_pacientes_dia,
                                            denominador = cli_total_saidas)
            cirurgico = self.kpi_tempo_medio( numerador = cir_total_pacientes_dia,
                                              denominador = cir_total_saidas)
            ped = self.kpi_tempo_medio( numerador = ped_total_pacientes_dia,
                                        denominador = ped_total_saidas)
            ad = self.kpi_tempo_medio( numerador = ad_total_pacientes_dia,
                                       denominador = ad_total_saidas)
            idoso = self.kpi_tempo_medio( numerador = idoso_total_pacientes_dia,
                                          denominador = idoso_total_saidas)
            
            return cli_pedi,cli_ad,cli_idoso,cir_pedi,cir_ad,cir_idoso,clinico,cirurgico,ped,ad,idoso
        else:
            return None

    def kpi5(self, **kwargs) -> int:
        # 5. Tempo médio de internação
        chaves_obrigatorias = [
            'cli_pedi_total_pacientes_dia','cli_pedi_total_saidas',
            'cli_ad_total_pacientes_dia','cli_ad_total_saidas',
            'cli_idoso_total_pacientes_dia','cli_idoso_total_saidas',
            'cir_pedi_total_pacientes_dia','cir_pedi_total_saidas',
            'cir_ad_total_pacientes_dia','cir_ad_total_saidas',
            'cir_idoso_total_pacientes_dia','cir_idoso_total_saidas',
            ]
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):
            # Calcular o KPI        
            cli_total_pacientes_dia = kwargs['cli_pedi_total_pacientes_dia']+kwargs['cli_ad_total_pacientes_dia']+kwargs['cli_idoso_total_pacientes_dia']
            cir_total_pacientes_dia = kwargs['cir_pedi_total_pacientes_dia']+kwargs['cir_ad_total_pacientes_dia']+kwargs['cir_idoso_total_pacientes_dia']
            ped_total_pacientes_dia = kwargs['cir_pedi_total_pacientes_dia']+kwargs['cli_pedi_total_pacientes_dia']
            ad_total_pacientes_dia = kwargs['cir_ad_total_pacientes_dia']+kwargs['cli_ad_total_pacientes_dia']
            idoso_total_pacientes_dia = kwargs['cir_idoso_total_pacientes_dia']+kwargs['cli_idoso_total_pacientes_dia']
            cli_total_saidas = kwargs['cli_pedi_total_saidas']+kwargs['cli_ad_total_saidas']+kwargs['cli_idoso_total_saidas']
            cir_total_saidas = kwargs['cir_pedi_total_saidas']+kwargs['cir_ad_total_saidas']+kwargs['cir_idoso_total_saidas']
            ped_total_saidas = kwargs['cir_pedi_total_saidas']+kwargs['cli_pedi_total_saidas']
            ad_total_saidas = kwargs['cir_ad_total_saidas']+kwargs['cli_ad_total_saidas']
            idoso_total_saidas = kwargs['cir_idoso_total_saidas']+kwargs['cli_idoso_total_saidas']

            cli_pedi = self.kpi_tempo_medio( numerador = kwargs['cli_pedi_total_pacientes_dia'],
                                            denominador = kwargs['cli_pedi_total_saidas'])
            cli_ad = self.kpi_tempo_medio( numerador = kwargs['cli_ad_total_pacientes_dia'],
                                           denominador = kwargs['cli_ad_total_saidas'])
            cli_idoso = self.kpi_tempo_medio( numerador = kwargs['cli_idoso_total_pacientes_dia'],
                                              denominador = kwargs['cli_idoso_total_saidas'])
            cir_pedi = self.kpi_tempo_medio( numerador = kwargs['cir_pedi_total_pacientes_dia'],
                                             denominador = kwargs['cir_pedi_total_saidas'])
            cir_ad = self.kpi_tempo_medio( numerador = kwargs['cir_ad_total_pacientes_dia'],
                                           denominador = kwargs['cir_ad_total_saidas'])
            cir_idoso = self.kpi_tempo_medio( numerador = kwargs['cir_idoso_total_pacientes_dia'],
                                              denominador = kwargs['cir_idoso_total_saidas'])
            clinico = self.kpi_tempo_medio( numerador = cli_total_pacientes_dia,
                                            denominador = cli_total_saidas)
            cirurgico = self.kpi_tempo_medio( numerador = cir_total_pacientes_dia,
                                              denominador = cir_total_saidas)
            ped = self.kpi_tempo_medio( numerador = ped_total_pacientes_dia,
                                        denominador = ped_total_saidas)
            ad = self.kpi_tempo_medio( numerador = ad_total_pacientes_dia,
                                       denominador = ad_total_saidas)
            idoso = self.kpi_tempo_medio( numerador = idoso_total_pacientes_dia,
                                          denominador = idoso_total_saidas)
            
            return cli_pedi,cli_ad,cli_idoso,cir_pedi,cir_ad,cir_idoso,clinico,cirurgico,ped,ad,idoso
        else:
            return None

    def kpi6(self, **kwargs) -> int:
        # 6. Tempo médio de permanência na emergência
        chaves_obrigatorias = ['total_tempo_entrada_ate_termino','total_pacientes_buscaram_atendimento']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):
            # Calcular o KPI        
            return self.kpi_tempo_medio( numerador = kwargs['total_tempo_entrada_ate_termino'],
                                         denominador = kwargs['total_pacientes_buscaram_atendimento'] )
        else:
            return None

    def kpi7(self, **kwargs) -> tuple:
        # 7. Tempo médio de espera na emergência para primeiro atendimento
        chaves_obrigatorias = ['nvl2_total_tempo_espera',
                               'nvl2_total_pacientes_buscaram_atendimento',
                               'nvl3_total_tempo_espera',
                               'nvl3_total_pacientes_buscaram_atendimento']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):
            total_tempo_espera = kwargs['nvl2_total_tempo_espera']+kwargs['nvl3_total_tempo_espera']
            total_pacientes_buscaram_atendimento = kwargs['nvl2_total_pacientes_buscaram_atendimento']+kwargs['nvl3_total_pacientes_buscaram_atendimento']
            nvl2 = self.kpi_tempo_medio( numerador = kwargs['nvl2_total_tempo_espera'],
                                         denominador = kwargs['nvl2_total_pacientes_buscaram_atendimento'])
            nvl3 = self.kpi_tempo_medio( numerador = kwargs['nvl3_total_tempo_espera'],
                                         denominador = kwargs['nvl2_total_pacientes_buscaram_atendimento'])
            geral = self.kpi_tempo_medio( numerador = total_tempo_espera,
                                          denominador = total_pacientes_buscaram_atendimento )
            return nvl2, nvl3, geral
        else:
            return None

    def kpi8(self, **kwargs) -> int:
        # 8. Taxa de início de antibiótico intravenoso profilático
        chaves_obrigatorias = ['total_cirurgias_limpas_com_atb','total_cirurgias_limpas']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            # Calcular o KPI        
            return self.kpi_taxa( numerador = kwargs['total_cirurgias_limpas_com_atb'],
                                  denominador = kwargs['total_cirurgias_limpas'] )
        else:
            return None

    def kpi9(self, **kwargs) -> int:
        # 9. Taxa de infecção de sítio cirúrgico em cirurgia limpa
        chaves_obrigatorias = ['total_isc_ate_30_dias','total_cirurgias_limpas_mes_anterior']

        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            # Calcular o KPI        
            return self.kpi_taxa( numerador = kwargs['total_isc_ate_30_dias'],
                                  denominador = kwargs['total_cirurgias_limpas_mes_anterior'] )      
        else:
            return None

    def kpi12(self, **kwargs) -> tuple:
        # 12. Taxa de profilaxia de tromboembolismo venoso
        chaves_obrigatorias = [ 'cli_total_pacientes_risco_profilaxia_TEV',
                                'cli_total_pacientes_risco',
                                'cir_orto_total_pacientes_risco_profilaxia_TEV',
                                'cir_orto_total_pacientes_risco',
                                'cir_n_orto_total_pacientes_risco_profilaxia_TEV',
                                'cir_n_orto_total_pacientes_risco']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            cir_total_pacientes_risco_profilaxia_TEV = kwargs['cir_orto_total_pacientes_risco_profilaxia_TEV']+kwargs['cir_n_orto_total_pacientes_risco_profilaxia_TEV']
            total_pacientes_risco_profilaxia_TEV = cir_total_pacientes_risco_profilaxia_TEV+kwargs['cli_total_pacientes_risco_profilaxia_TEV']
            cir_total_pacientes_risco = kwargs['cir_orto_total_pacientes_risco']+kwargs['cir_n_orto_total_pacientes_risco']
            total_pacientes_risco = cir_total_pacientes_risco+kwargs['cli_total_pacientes_risco']
            cir_orto = self.kpi_taxa( numerador = kwargs['cir_orto_total_pacientes_risco_profilaxia_TEV'],
                                      denominador = kwargs['cir_orto_total_pacientes_risco'])
            cir_n_orto = self.kpi_taxa( numerador = kwargs['cir_n_orto_total_pacientes_risco_profilaxia_TEV'],
                                        denominador = kwargs['cir_n_orto_total_pacientes_risco'])
            cirurgico = self.kpi_taxa( numerador = cir_total_pacientes_risco_profilaxia_TEV,
                                 denominador = cir_total_pacientes_risco)
            geral = self.kpi_taxa( numerador = total_pacientes_risco_profilaxia_TEV,
                                   denominador = total_pacientes_risco )
            return cir_orto, cir_n_orto, cirurgico, geral
        else:
            return None
        
    def kpi13(self, **kwargs) -> int:
        # 13. Densidade de incidência de queda resultando em lesão em paciente
        chaves_obrigatorias = ['total_quedas_dano','total_pacientes_dia']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            # Calcular o KPI        
            return self.kpi_densidade( numerador = kwargs['total_quedas_dano'],
                                       denominador = kwargs['total_pacientes_dia'] )  
        else:
            return None

    def kpi14(self, **kwargs) -> int:
        # 14. Evento sentinela
        chaves_obrigatorias = ['total_eventos_sentinela','total_pacientes_dia']
        if (self.validar_kwargs(kwargs,chaves_obrigatorias)):        
            # Calcular o KPI        
            return self.kpi_densidade( numerador = kwargs['total_eventos_sentinela'],
                                       denominador = kwargs['total_pacientes_dia'] )  
        else:
            return None     

    def calcular( self, metrics:pd.DataFrame ) -> list[float]:

        if (metrics):
        # 1. Proporção de partos vaginais 
        # 2. Proporção de reinternações em até 30 dias da saída hospitalar
        # 3. Taxa de parada cardiorrespiratória em unidade de internação

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

            kpi4 = ((
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
            ))[0] *100

        # 5. Tempo médio de internação
        # 6. Tempo médio de permanência na emergência
        # 7. Tempo médio de espera na emergência para primeiro atendimento
        # 8. Taxa de início de antibiótico intravenoso profilático
        # 9. Taxa de infecção de sítio cirúrgico em cirurgia limpa

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

            kpi10 = (
                (   metrics.unid_int_neo_precoce_infec+
                    metrics.unid_int_neo_tardio_infec+
                    metrics.unid_int_pedi_infec+
                    metrics.unid_int_ad_infec+
                    metrics.unid_int_idoso_infec+
                    metrics.uti_neo_precoce_infec+
                    metrics.uti_neo_tardio_infec+
                    metrics.uti_pedi_infec+
                    metrics.uti_ad_infec+
                    metrics.uti_idoso_infec
                ) /                 
                (   metrics.unid_int_neo_precoce_cvc_dia+
                    metrics.unid_int_neo_tardio_cvc_dia+
                    metrics.unid_int_pedi_cvc_dia+
                    metrics.unid_int_ad_cvc_dia+
                    metrics.unid_int_idoso_cvc_dia+
                    metrics.uti_neo_precoce_cvc_dia+
                    metrics.uti_neo_tardio_cvc_dia+
                    metrics.uti_pedi_cvc_dia+
                    metrics.uti_ad_cvc_dia+
                    metrics.uti_idoso_cvc_dia
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
            kpi11 = (
                (   metrics.unid_int_neo_precoce_itu+
                    metrics.unid_int_neo_tardio_itu+
                    metrics.unid_int_pedi_itu+
                    metrics.unid_int_ad_itu+
                    metrics.unid_int_idoso_itu+
                    metrics.uti_neo_precoce_itu+
                    metrics.uti_neo_tardio_itu+
                    metrics.uti_pedi_itu+
                    metrics.uti_ad_itu+
                    metrics.uti_idoso_itu
                ) /                 
                (   metrics.unid_int_neo_precoce_cvd_dia+
                    metrics.unid_int_neo_tardio_cvd_dia+
                    metrics.unid_int_pedi_cvd_dia+
                    metrics.unid_int_ad_cvd_dia+
                    metrics.unid_int_idoso_cvd_dia+
                    metrics.uti_neo_precoce_cvd_dia+
                    metrics.uti_neo_tardio_cvd_dia+
                    metrics.uti_pedi_cvd_dia+
                    metrics.uti_ad_cvd_dia+
                    metrics.uti_idoso_cvd_dia
                )
            )[0] *1000

        # 12. Taxa de profilaxia de tromboembolismo venoso

        # 13. Densidade de incidência de queda resultando em lesão em paciente            
            #( metrics.cli_neo_precoce_pacientes_dia+
            #metrics.cli_neo_tardio_pacientes_dia+
            #metrics.cli_pedi_pacientes_dia+
            #metrics.cli_ad_pacientes_dia+
            #metrics.cli_idoso_pacientes_dia+
            #metrics.cir_neo_precoce_pacientes_dia+
            #metrics.cir_neo_tardio_pacientes_dia+
            #metrics.cir_pedi_pacientes_dia+
            #metrics.cir_ad_pacientes_dia+
            #metrics.cir_idoso_pacientes_dia )

        # 14. Evento sentinela
            #( metrics.cli_neo_precoce_pacientes_dia+
            #metrics.cli_neo_tardio_pacientes_dia+
            #metrics.cli_pedi_pacientes_dia+
            #metrics.cli_ad_pacientes_dia+
            #metrics.cli_idoso_pacientes_dia+
            #metrics.cir_neo_precoce_pacientes_dia+
            #metrics.cir_neo_tardio_pacientes_dia+
            #metrics.cir_pedi_pacientes_dia+
            #metrics.cir_ad_pacientes_dia+
            #metrics.cir_idoso_pacientes_dia )

        else:
            raise Exception("Dados em branco")
    
        kpis = [kpi1, 
                kpi2_cli, kpi2_cir, kpi2,
                kpi3,
                kpi4_cli_neo_precoce, kpi4_cli_neo_tardio, kpi4_cli_pedi, kpi4_cli_adulto, kpi4_cli_idoso, kpi4_cli,
                kpi4_cir_neo_precoce, kpi4_cir_neo_tardio, kpi4_cir_pedi, kpi4_cir_adulto, kpi4_cir_idoso, kpi4_cir,
                kpi4_neo_precoce, kpi4_neo_tardio, kpi4_pedi, kpi4_ad, kpi4_idoso, kpi4,
                kpi5_cli_pedi, kpi5_cli_adulto, kpi5_cli_idoso, kpi5_cli,
                kpi5_cir_pedi, kpi5_cir_adulto, kpi5_cir_idoso, kpi5_cir,
                kpi5_pedi, kpi5_ad, kpi5_idoso, kpi5,
                kpi6,
                kpi7_nvl2, kpi7_nvl3, kpi7,
                kpi8,
                kpi9,
                kpi10_neo, kpi10_pedi, kpi10_ad, kpi10_neo_uti, kpi10_pedi_uti, kpi10_ad_uti, kpi10_unid_int, kpi10_uti, kpi10,
                kpi11_neo, kpi11_pedi, kpi11_ad, kpi11_neo_uti, kpi11_pedi_uti, kpi11_ad_uti, kpi11_unid_int, kpi11_uti, kpi11,
                kpi12_cli, kpi12_cir_orto, kpi12_cir_nao_orto, kpi12,
                kpi13,
                kpi14]
        
        return kpis
        
