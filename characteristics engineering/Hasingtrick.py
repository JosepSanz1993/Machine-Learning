from sklearn.feature_extraction import FeatureHasher
class Has_trick:
    def __init__(self,data,n_features,input_type):
        self.__data = data
        if input_type !='string':
            self.__tick = FeatureHasher(n_features=n_features)
        else:
             self.__tick = FeatureHasher(n_features=n_features, input_type=input_type)
    def train(self):
        self.__tick.fit(self.__data)
    def transform_data(self):
        return self.__tick.transform(self.__data)
    def get_matrix_info(self):
        print(self.transform_data().todense())

data = [{'dog':34,'cat':30,'dolphin':77},
        {'cat':44,'shark':78,'dolphin':100},
        {'dog':56,'shark':26,'dog':56}]
hasing_trick = Has_trick(data,10,'dict')
hasing_trick.train()
hasing_trick.get_matrix_info()

data = [['cat','dog','bird'],['cat','bird'],['fish','dog']]
hasing_trick = Has_trick(data,4,'string')
hasing_trick.train()
hasing_trick.get_matrix_info()