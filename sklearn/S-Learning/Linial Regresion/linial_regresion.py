import numpy as np 
from dataframe import dataframe
from sklearn.linear_model import LinearRegression
class linial_reg(dataframe):
    def __init__(self,file,data):
        super().__init__(file)
        self.__df = self.create_dataframe(data)
    def __make_sklearn(self,key_x,key_y):
        clf = LinearRegression()
        train = clf.fit(np.reshape(self.__df[key_x],(-1,1)),
                        np.reshape(self.__df[key_y],(-1,1)))
        return train
    def show_coef(self,key_x,key_y):
        return self.__make_sklearn(key_x,key_y).coef_
    def show_intercept(self,key_x,key_y):
        return self.__make_sklearn(key_x,key_y).intercept_
    def make_prediction(self,key_x,key_y,value):
        return self.__make_sklearn(key_x,key_y).predict(value)
    
        
                

        
