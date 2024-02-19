from datafarme import data
import matplotlib.pyplot as plt
import seaborn as sb
class graphic(data):
    def __init__(self, file):
        super().__init__(file)
    def show_hist(self,field):
        self.get_dataframe().drop(field,axis=1).hist()
        plt.show()
g = graphic('usuarios_win_mac_lin.csv')
g.show_hist('clase')
