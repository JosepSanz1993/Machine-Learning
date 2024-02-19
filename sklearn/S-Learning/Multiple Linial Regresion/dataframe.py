from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import constant as const
class dataframe:
    def __init__(self,bd_name,col_name):
        client = MongoClient(const.url,server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
        except Exception as e:
            print(e)
        self.__bd = MongoClient(const.url)[bd_name]
        self.__collection = self.__bd[col_name]
    def change_collection(self,col_name):
        self.__collection = self.__bd[col_name]
    def create_collection(self,col_name):
        self.__bd.create_collection(col_name)
    def show_All_collection(self):
        return self.__collection.find()
    def show_query_from_collection(self,query):
        return self.__collection.find(query)
    def get_dataframe(self):
        df = pd.DataFrame(list(self.__collection.find()))
        df[const.replace_camp] = df[const.replace_camp].replace(const.dict)
        return df



