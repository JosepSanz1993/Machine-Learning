from dataframe import dataframe,const
from graphic import graphic
from multiple_linial_regression import multiple_l_reg
#Initial situation
df = dataframe("Iris","Data")
initial_perfomance = graphic() 
data_fd = df.get_dataframe()
#initial_perfomance.show_graphic(data_fd)
#Multiple linial regresion
data_fd = data_fd.drop("_id",axis='columns')
mlr = multiple_l_reg(data_fd,const.colum) 
vars = mlr.make_test_and_train_var()
train = mlr.make_mlp(vars[0],vars[2])
#predictions
train_pred = mlr.make_prediction_train(train,vars[0])
test_pred = mlr.make_prediction_test(train,vars[1])
#sore and check result
r2_score = mlr.r2_score_result(vars[3],test_pred)
print(r2_score)
mlp_score = mlr.mlp_score_result(train,vars[0],vars[2])
print(mlp_score)
#descomposition
desc = mlr.make_descomposition(1)
print(desc)


