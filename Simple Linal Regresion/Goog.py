import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error,r2_score
class goog:
    def __init__(self,url,num_row):
        self.__url = url
        self.__df = self.get_data_csv()
        self.get_info_df(num_row)
        self.__model = self.__liniar_regression_model()
    def get_url(self):
        return self.__url
    def set_url(self,url):
        self.__url = url
    def get_model(self):
        return self.__model
    def set_model(self,model):
        self.__model = model
    def get_df(self):
        return self.__df
    def get_train_test_volume_data(self,percent):
        volume_train = len(self.__df)*percent/100
        volume_test = len(self.__df)*(100-percent)/100
        return (round(volume_train),round(volume_test))
    def get_data_csv(self):
        try:
           df = pd.read_csv(self.__url)
        except FileNotFoundError:
            df = None
        except:
            print("The file not is a csv file")
        return df
    def get_info_df(self,num_row):
        print("The file size is {}\n".format(self.__df.shape))
        print("The firts {} rows are:\n".format(num_row))
        print(self.__df.head(num_row))
        print("Those are the basic statistics from input data:\n")
        print(self.__df.describe())
    def get_x(self,lambda_expresion,name_colum):
        return list(filter(lambda_expresion,self.__df[name_colum].dropna().drop_duplicates()))
    def get_y(self,name_colum):
        return self.__df[name_colum].dropna().drop_duplicates()
    def get_data_standarition(self,lambda_expresion,iterator):
        return list(map(lambda_expresion,iterator))
    def get_x_train(self,lamba_stand,lamba_exp,name_colum,ini,final):
        x = np.array(self.get_data_standarition(lamba_stand,self.get_x(lamba_exp,name_colum))).reshape(-1,1)
        return x[ini:final]
    def get_y_train(self,lamba_stand,name_colum,ini,final):
        y = np.array(self.get_data_standarition(lamba_stand,self.get_y(name_colum))).reshape(-1,1)
        return y[ini:final]
    def get_x_test(self,lamba_stand,lamba_exp,name_colum,ini,final):
        return self.get_x_train(lamba_stand,lamba_exp,name_colum,ini,final)
    def get_y_test(self,lamba_stand,name_colum,ini,final):
        return self.get_y_train(lamba_stand,name_colum,ini,final)
    def __liniar_regression_model(self):
        reg = LinearRegression()
        return reg
    def train_model(self,x_tain,y_train):
        self.__model.fit(x_tain,y_train)
    def get_prediction(self,x_test):
        predict = self.__model.predict(x_test)
        return (predict,len(predict))
    def show_prediction_result(self,predict,y_test):
        print('Coefficients ====>{}\n'.format(self.__model.coef_))
        print('Independet term ====>{}\n'.format(self.__model.intercept_))
        print("Mean squared error ====> %.2f" % mean_squared_error(y_test,predict))
        print('Variance sore =====> %.2f' % r2_score(y_test,predict))