import pandas as pd
class data:
    def __init__(self,file): 
        self.__dataframe = pd.read_csv(file)
    def show_head(self, lines_number):
        return self.__dataframe.head(lines_number)
    def show_describe(self):
        return self.__dataframe.describe()
    def groupby_size(self,field):
        return self.__dataframe.groupby(field).size()
    def get_dataframe(self):
        return self.__dataframe
