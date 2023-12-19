from data import temperature_data
import tensorflow as tf 
from data import plt
class temperature_model(temperature_data):
    def __init__(self, file):
        super().__init__(file)
    def __get_X_train(self,x):
        return self.get_x(x)
    def __get_Y_train(self,y):
        return self.get_y(y)
    def create_model(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(units=1,input_shape=[1]))
        return model
    def compile_model(self,model):
        model.compile(optimizer=tf.keras.optimizers.Adam(1),loss='mean_squared_error')
    def show_model(self,model):
        model.summary()
    def train_model(self,model,n_epochs,x,y):
        epochs_hist = model.fit(self.__get_X_train(x),self.__get_Y_train(y),epochs=n_epochs)
        return epochs_hist
    def evaluate_model(self,ep_hist,model):
        plt.plot(ep_hist.history['loss'])
        plt.title('Lost progress while train model')
        plt.xlabel('Epoch')
        plt.ylabel('Training Loss')
        plt.legend('Traning Loss')
        model.get_weights()
        plt.show()
    def make_prediction(self,model,temp_c):
        return model.predict([temp_c])