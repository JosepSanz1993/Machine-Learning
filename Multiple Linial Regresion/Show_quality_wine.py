from model_quality_wine import model_quality_wine
import matplotlib.pyplot as plt
class show_quality_wine(model_quality_wine):
    def __init__(self, url,name_colum):
        super().__init__(url)
        self.__data = self.train_and_test_var(name_colum)
        self.__y_pred = self.__linal_model_quality_wine()
    def __linal_model_quality_wine(self):
        model = self.get_linial_model()
        self.train_model(model,self.__data)
        y_pred = self.get_prediction(model,self.__data)
        return y_pred
    def graphic_quality_wine(self):
        plt.scatter(self.__data[3],self.__y_pred,color ='green')
        plt.xlabel("Real Values")
        plt.ylabel("Predictions")
        plt.title("Multiple Linial Regression")
        plt.show()
    def show_evalution_model(self):
        mse,r2=self.evaluate_model(self.__data,self.__y_pred)
        print("MSE ==> {}".format(mse))
        print("R2 Score ==> {}".format(r2))
