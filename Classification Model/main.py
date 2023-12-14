from Generationdata import generation_patient_data as gpd
from Classificationmodel import classification_model as cm

#class generation data instance
data = gpd([2000,5,5,0,42],'data.json','colum')
#generate random data
x,y = data.make_classification()
#generate data error
df = data.generate_dataframe_error(data.generate_dataframe(x),42,10)
#correc of dataframe
df = data.correct_dataframa_error(df)
#class classificaction model instance
instance_model = cm(df,y)
#train and test var for model
x_train,x_test,y_train,y_test = instance_model.train_test_var_classification_model()
#create a classification model 
model = instance_model.create_classification_model(100,42)
#train model
instance_model.train_classification_model(model,x_train,y_train)
#make predicction
y_pred = instance_model.make_prediction(model,x_test)
#evaluate classification model--> show classification report
report = instance_model.show_classification_report(y_pred,y_test)
print(report)
#evaluate classifcation model--> Calculate AUC-ROC Metric
curve_auc_roc = instance_model.calculate_auc_roc_curve(y_pred,y_test)
print("The value of curve AUC-ROC is: {}".format(curve_auc_roc))
#evaluate classifcation model--> show AUC-ROC Metric
instance_model.show_curve_roc(model,x_test,y_test)