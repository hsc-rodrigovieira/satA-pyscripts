import pymongo as db
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

    def get_data(self, collection_name:str, query:dict) -> dict:
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
                client = db.MongoClient(config.MONGO_URI)
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


