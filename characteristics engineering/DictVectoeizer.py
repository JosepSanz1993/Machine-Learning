from sklearn.feature_extraction import DictVectorizer
class vect:
    def __init__(self,data):
        self.__data = data
        self.__vect = DictVectorizer(sparse=False)
    def train(self):
        self.__vect.fit(self.__data)
    def transform_data(self):
        return self.__vect.transform(self.__data)
    def get_type(self):
        print(type(self.transform_data()))
    def get_colum_info(self):
        print(self.__vect.feature_names_)
    def get_colum_vocabulary(self):
        print(self.__vect.vocabulary_)

data = [{'name':'Josep','age':30,'city':'Tarragona'},
        {'name':'Joan','age':26,'city':'LAldea'},
        {'name':'Qiao','age':26,'city':'Reus'}]
v = vect(data)
v.train()
print(v.transform_data())
v.get_type()
v.get_colum_info()
v.get_colum_vocabulary()

