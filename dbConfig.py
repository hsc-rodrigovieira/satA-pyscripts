import pymongo as db
import streamlit as st
import config
from bson.objectid import ObjectId

class dbConfig (object):

    def __init__(self):
        self.conn_string = config.MONGO_URI
        self.database = config.DATABASE        
        pass

    def validar_query(self, dicionario:dict, chaves_obrigatorias:list) -> bool:
        # Validar se kwargs está vazio
        if not dicionario:
            raise ValueError("O dicionário não pode estar vazio.")
        
        # Validar se todas as chaves obrigatórias estão presentes
        for chave in chaves_obrigatorias:
            if chave not in dicionario:
                raise KeyError(f"A chave '{chave}' está ausente.")
        
        # Validar se os valores das chaves obrigatórias não são nulos
        for chave in chaves_obrigatorias:
            if dicionario[chave] is None:
                raise ValueError(f"O valor da chave '{chave}' não pode ser nulo.")
            
        # Retornar True se tudo estiver válido
        return True

    def get_metrics(self, collection_name:str, query:dict) -> dict:
        chaves_obrigatorias = [
            "organization_id",
            "year",
            "month"
        ]
        # Validar existência dos parâmetros
        if not collection_name or not query:
            raise ValueError("Os parametros não podem estar vazios.")
        
        if(self.validar_query(query,chaves_obrigatorias)):
            # Validar se os valores das chaves obrigatórias não são nulos
            if type(query["organization_id"]) is not ObjectId:
                    raise ValueError(f"Tipo da chave 'organization_id' incorreto. Esperado ObjectId.")
            if type(query["year"]) is not int:
                    raise ValueError(f"Tipo da chave 'year' incorreto. Esperado int.")
            if type(query["month"]) is not int:
                    raise ValueError(f"Tipo da chave 'month' incorreto. Esperado int.")
            try:
                client = db.MongoClient(self.conn_string)
                database = client.get_database(self.database)
                collection = database.get_collection(collection_name)
                metrics = collection.find_one(query)
                client.close()
            except Exception as e:
                raise Exception("Unable to retrieve the document due to the following error: ", e)
            if (not metrics):
                raise Exception("Collection not found.")
            else:
                return metrics
        else:
            None

    @st.cache_data
    def get_organizations(_self, collection_name:str) -> dict:           
        query = {"status":"Active"}
        try:
            client = db.MongoClient(_self.conn_string)
            database = client.get_database(_self.database)
            collection = database.get_collection(collection_name)
            organizations = collection.find(query)
            names = [f"{i['name']} ({i['cnes']})" for i in organizations]
            client.close()
        except Exception as e:
            raise Exception("Unable to retrieve the document due to the following error: ", e)
        return names
    
    @st.cache_data
    def get_last_consolidation(_self, collection_name:str, cnes:int) -> list:           
        query = {"organization_cnes": int(cnes)}
        fields = {"year":1,"month":1,"_id":0}
        sorting = [("year",db.DESCENDING),("month",db.DESCENDING)]
        try:
            client = db.MongoClient(_self.conn_string)
            database = client.get_database(_self.database)
            collection = database.get_collection(collection_name)
            last_consolidation = collection.find(query,fields).sort(sorting)
            year_month = list(last_consolidation)
            client.close()
        except Exception as e:
            raise Exception("Unable to retrieve the document due to the following error: ", e)
        return year_month

    def load_data(self, collection_name:str, query:dict) -> bool:
        chaves_obrigatorias = [
            'organization_id', 'year', 'month', 'rkpi1', 'rkpi2_clinico',
            'rkpi2_cirurgico', 'rkpi2_geral', 'rkpi3', 'rkpi4_cli_neo_precoce',
            'rkpi4_cli_neo_tardio', 'rkpi4_cli_pedi', 'rkpi4_cli_ad', 'rkpi4_cli_idoso',
            'rkpi4_cir_neo_precoce', 'rkpi4_cir_neo_tardio', 'rkpi4_cir_pedi',
            'rkpi4_cir_ad', 'rkpi4_cir_idoso', 'rkpi4_clinico', 'rkpi4_cirurgico',
            'rkpi4_neo_precoce', 'rkpi4_neo_tardio', 'rkpi4_pedi', 'rkpi4_ad',
            'rkpi4_idoso', 'rkpi4_geral', 'rkpi5_cli_pedi', 'rkpi5_cli_ad', 
            'rkpi5_cli_idoso', 'rkpi5_cir_pedi', 'rkpi5_cir_ad', 'rkpi5_cir_idoso',
            'rkpi5_clinico', 'rkpi5_cirurgico', 'rkpi5_pedi', 'rkpi5_ad', 'rkpi5_idoso',
            'rkpi5_geral', 'rkpi6', 'rkpi7_nvl2', 'rkpi7_nvl3', 'rkpi7_geral', 'rkpi8',
            'rkpi9', 'rkpi10_ui_neo', 'rkpi10_ui_pedi', 'rkpi10_ui_ad', 'rkpi10_uti_neo',
            'rkpi10_uti_pedi', 'rkpi10_uti_ad', 'rkpi10_neo', 'rkpi10_pedi', 'rkpi10_ad',
            'rkpi10_ui', 'rkpi10_uti', 'rkpi10_geral', 'rkpi11_ui_neo', 'rkpi11_ui_pedi',
            'rkpi11_ui_ad', 'rkpi11_uti_neo', 'rkpi11_uti_pedi', 'rkpi11_uti_ad',
            'rkpi11_neo', 'rkpi11_pedi', 'rkpi11_ad', 'rkpi11_ui', 'rkpi11_uti',
            'rkpi11_geral', 'rkpi12_cir_orto', 'rkpi12_cir_n_orto', 'rkpi12_cirurgico',
            'rkpi12_geral', 'rkpi13', 'rkpi14'
        ]
        # Validar existência dos parâmetros
        if not collection_name or not query:
            raise ValueError("Os parametros não podem estar vazios.")
        if(self.validar_query(query,chaves_obrigatorias)):
            # Validar se os valores das chaves obrigatórias não são nulos
            if type(query["organization_id"]) is not ObjectId:
                raise ValueError(f"Tipo da chave 'organization_id' incorreto. Esperado ObjectId.")
        try:
            client = db.MongoClient(self.conn_string)
            database = client.get_database(self.database)
            collection = database.get_collection(collection_name)
            result = collection.insert_one(query)
            client.close()
        except Exception as e:
            raise Exception("Unable to retrieve the document due to the following error: ", e)
        if (not result.acknowledged):
            raise Exception("DB return missing.") 
        else:
            return result.acknowledged
