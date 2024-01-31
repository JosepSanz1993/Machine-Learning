from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import decomposition
from sklearn.metrics import r2_score
class multiple_l_reg:
    def __init__(self,df,colum):
        self.__X = df.drop(colum,axis='columns')
        self.__y = df[colum]
    def make_test_and_train_var(self):
        X_train,X_test,y_train,y_test = train_test_split(self.__X,self.__y,test_size=0.30,random_state=40)
        return(X_train,X_test,y_train,y_test)
    def make_mlp(self,X_train,y_train):
        mlp = MLPRegressor(solver='adam',alpha=1e-4,hidden_layer_sizes=(60),max_iter=200,tol=1e-4,random_state=1)
        return mlp.fit(X_train,y_train)
    def make_prediction_train(self,mlp,X_train):
        return mlp.predict(X_train)
    def make_prediction_test(self,mlp,X_test):
        return mlp.predict(X_test)
    def r2_score_result(self,y_test,predict_test):
        return r2_score(y_test,predict_test)
    def mlp_score_result(self,mlp,X_train,y_train):
        return mlp.score(X_train,y_train)
    def make_descomposition(self,n_component):
        pca = decomposition.PCA(n_components=n_component)
        return pca.fit_transform(self.__X)
    
