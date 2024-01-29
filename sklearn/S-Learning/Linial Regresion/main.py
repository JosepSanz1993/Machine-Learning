#import Libraries
from graphic import graphic
from dataframe import dataframe
from linial_regresion import linial_reg
import constant as const
#dataframe  instance class,create dataframe and show information
data = dataframe(const.file)
df = data.create_dataframe(const.diccionary)
print(data.get_dataframe_info(df))
#show initial situation graphic
show_graphic = graphic(df,const.x,const.y)
show_graphic.get_scatter_graphic(const.x,const.y)
#Linial regresion with Skelearn
l_reg = linial_reg(const.file,const.diccionary)
coef= l_reg.show_coef(const.x,const.y)
intercept = l_reg.show_intercept(const.x,const.y)
print("coef is {} and intercept {}".format(coef,intercept))
print(l_reg.make_prediction(const.x,const.y,[[7]]))
#result graphic
show_graphic.get_plot(const.x,const.y,const.title,const.legend,df[const.x])