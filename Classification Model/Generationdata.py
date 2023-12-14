import pandas as pd
import numpy as np
import json
from sklearn.datasets import make_classification
class generation_patient_data:
    def __init__(self,data,file,key):
        self.__data = data
        self.__file = file
        self.__colum =self.__get_colum(key)
    def make_classification(self):
        x,y = make_classification(n_samples=self.__data[0],n_features=self.__data[1],
                                  n_informative=self.__data[2],n_redundant=self.__data[3],
                                  random_state=self.__data[4])
        return (x,y)
    def __get_colum(self,key):
        with open(self.__file,'r',encoding="utf-8")as f:
            colum = json.load(f).get(key)
        return colum
    def generate_dataframe(self,x):
        df = pd.DataFrame(x,columns=self.__colum)
        return df.abs()
    def generate_dataframe_error(self,df,seed,size):
        np.random.seed(seed)
        rows = np.random.choice(df.index,size=size)
        df.loc[rows,self.__colum[0]] = df.loc[rows,self.__colum[0]]*100
        df.loc[rows,self.__colum[1]] = df.loc[rows,self.__colum[1]]*150
        df.loc[rows,self.__colum[2]] = df.loc[rows,self.__colum[2]]*10
        df.loc[rows,self.__colum[3]] = df.loc[rows,self.__colum[3]]*5
        df.loc[rows,self.__colum[4]] = df.loc[rows,self.__colum[4]]*5
        return df
    def correct_dataframa_error(self,df):
        df[self.__colum[0]] = df[self.__colum[0]].apply(lambda x:x if x<200 else x/100)
        df[self.__colum[1]] = df[self.__colum[1]].apply(lambda x:x if x<150 else x/150)
        df[self.__colum[2]] = df[self.__colum[2]].apply(lambda x:x if x<10 else x/10)
        df[self.__colum[3]] = df[self.__colum[3]].apply(lambda x:x if x<5 else x/5)
        df[self.__colum[4]] = df[self.__colum[4]].apply(lambda x:x if x<5 else x/5)
        return df