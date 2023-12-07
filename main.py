from constant import url,lambda_f,lambda_s,name,num_row,volume
from Goog_visual import VisualGoog
#create a class visualGoog and show data dataframe
visual_goog = VisualGoog(url,num_row)
#show hiostograme
visual_goog.distribution_price_bar(name)
#var x nad y
x = visual_goog.get_data_standarition(lambda_s,visual_goog.get_x(lambda_s,name))
y = visual_goog.get_data_standarition(lambda_s,visual_goog.get_y(name))
#Calculate data volume for trian and test
volum = visual_goog.get_train_test_volume_data(volume)
#var x_train, y_train
x_train = visual_goog.get_x_train(lambda_s,lambda_f,name,0,volum[0])
y_train = visual_goog.get_y_train(lambda_s,name,0,volum[0])
#var x_test,y_test
x_test = visual_goog.get_x_test(lambda_s,lambda_f,name,volum[0],(volum[0]+volum[1])-1)
y_test = visual_goog.get_y_test(lambda_s,name,volum[0],(volum[0]+volum[1])-1)
#tarin model
visual_goog.train_model(x_train,y_train)
#do prediction
y_predict = visual_goog.get_prediction(x_test)
#show result
visual_goog.show_prediction_result(y_predict[0],y_test[0:y_predict[1]])
visual_goog.scatter_graphic_real_and_predic_values([x,y,y_test[0:len(y_predict[0])],y_predict[0]])