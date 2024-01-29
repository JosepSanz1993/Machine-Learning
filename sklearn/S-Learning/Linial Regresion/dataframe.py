import json
import pandas as pd
class dataframe:
    def __init__(self,file):
        self.file = file
    def __get_json_values(self):
        with open(self.file) as f:
           values =  json.load(f)
        return values
    def create_dataframe(self,data):
        return pd.DataFrame(self.__get_json_values()[data])
    def get_dataframe_info(self,dataframe):
        return dataframe.info()