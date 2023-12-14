from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,roc_auc_score
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt
class classification_model:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def train_test_var_classification_model(self):
        X_train,X_test,Y_train,Y_test = train_test_split(self.__x,self.__y,test_size=0.2,random_state=42)
        return (X_train,X_test,Y_train,Y_test)
    def create_classification_model(self,n_estimators,rand):
        model = RandomForestClassifier(n_estimators=n_estimators,random_state=rand)
        return model
    def train_classification_model(self,model,X_train,Y_train):
        model.fit(X_train,Y_train)
    def make_prediction(self,model,X_test):
        y_pred = model.predict(X_test)
        return y_pred
    def show_classification_report(self,y_pred,Y_test):
        return classification_report(Y_test,y_pred)
    def calculate_auc_roc_curve(self,y_pred,Y_test):
        roc_auc = roc_auc_score(Y_test,y_pred)
        return roc_auc
    def show_curve_roc(self,model,X_test,Y_test):
        curve_graphic = RocCurveDisplay.from_estimator(model,X_test,Y_test)
        plt.show()
    