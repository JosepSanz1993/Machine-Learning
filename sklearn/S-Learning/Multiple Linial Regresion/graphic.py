import seaborn as sns
import matplotlib.pyplot as plt
class graphic:
    def show_graphic(self,df):
        sns.pairplot(df)
        plt.show()