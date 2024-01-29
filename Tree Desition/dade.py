import redis,random
temp = []
class dade:
    def __init__(self):
        self.__r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    def create_array(self,number):
        for i in range(number):
            for j in range(3):
                value = random.choice([0,1,2])
                temp.append(value)
            self.__r.rpush("val",str(temp))
            temp.clear()
        print(self.__r.lrange("val","0","2"))
d = dade()
d.create_array(10)