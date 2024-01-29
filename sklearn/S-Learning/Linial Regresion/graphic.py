import matplotlib.pyplot as plt
class graphic:
    def __init__(self,dataframe,x,y):
        self.__x = dataframe[x]
        self.__y = dataframe[y]
    def get_scatter_graphic(self,x_label,y_label):
        plt.scatter(self.__x,self.__y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid()
        plt.show()
    def get_plot(self,x_label,y_label,title,legend,predict):
        plt.plot(self.__x,self.__y)
        plt.plot(self.__x,predict)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(legend)
        plt.grid()
        plt.show()
    