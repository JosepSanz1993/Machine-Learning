import matplotlib.pyplot as plt
from Goog import goog
class VisualGoog(goog):
    def __init__(self, url, num_row):
        super().__init__(url, num_row)
    def distribution_price_bar(self,name_colum):
        plt.hist(self.get_df()[name_colum],color='green')
        plt.title('Distribuiton prices')
        plt.xlabel('prices')
        plt.ylabel('Freq')
        plt.show()
    def scatter_graphic_real_and_predic_values(self,data):
        plt.scatter(data[0],data[1],color='orange',label='originals data')
        plt.plot(data[2],data[3],color='red',linewidth=2,label='Linial Regretion')
        plt.title('Graphic of prices prediction')
        plt.xlabel('Price Between 20 and 80')
        plt.ylabel('All Prices')
        plt.legend()
        plt.show()
