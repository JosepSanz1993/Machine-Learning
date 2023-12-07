import pandas as pd
import requests,io
class Load:
    def __init__(self,url):
        self.__url = requests.get(url).content
        self.__df = self.__get_data_file()
    def get_url(self):
        return self.__url
    def set_url(self,url):
        self.__url = requests.get(url).content
        self.__df = self.__get_data_file()
    def __get_data_file(self):
        try:
            df = pd.read_csv(io.StringIO(self.__url.decode('utf8')),delimiter=';')
            df = pd.DataFrame(df).dropna()
        except:
            df = pd.DataFrame()
        return df
    def show_basic_exploration_analysis(self):
        print(self.__df.head())
        print(self.__df.describe())
    def get_dataframe(self):
        return self.__df
