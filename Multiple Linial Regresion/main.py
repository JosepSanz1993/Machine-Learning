from constant import name_colum,wine_quality_url
from Show_quality_wine import show_quality_wine
#The instance of show quality wine class
graphic = show_quality_wine(wine_quality_url,name_colum)
#The basic exploration analysis
graphic.show_basic_exploration_analysis()
#graphic of quality of wine
graphic.graphic_quality_wine()
#mse and r2 score
graphic.show_evalution_model()