from Load_quality_wine import Load
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
class model_quality_wine(Load):
    def __init__(self, url):
        super().__init__(url)
    def get_x(self,name_colum):
        return self.get_dataframe().drop(name_colum,axis=1)
    def get_y(self,name_colunm):
        return self.get_dataframe()[name_colunm]
    def train_and_test_var(self,name_colum):
        x_train,x_test,y_train,y_test = train_test_split(self.get_x(name_colum),self.get_y(name_colum),
        test_size=0.2,random_state=42)
        return(x_train,x_test,y_train,y_test)
    def get_linial_model(self):
        model = LinearRegression()
        return model
    def train_model(self,model,data):
        return model.fit(data[0],data[2])
    def get_prediction(self,model,data):
        return model.predict(data[1])
    def evaluate_model(self,data,y_pred):
        mse = mean_squared_error(data[3],y_pred)
        r2 = r2_score(data[3],y_pred)
        return (mse,r2)
