from model import temperature_model
m_temp = temperature_model("/Volumes/MACHINE/Machine Learning course/Others_exercises/Ex1/celsius_a_fahrenheit.csv")
#show temperature data
m_temp.show_temperature_data('Celsius','Fahrenheit')
#create, summary and compile model
model = m_temp.create_model()
m_temp.show_model(model)
m_temp.compile_model(model)
#train model
train = m_temp.train_model(model,100,'Celsius','Fahrenheit')
#evaluate model 
m_temp.evaluate_model(train,model)
#make prediction
print(m_temp.make_prediction(model,0))