import requests
from faker import Faker
import random
faker = Faker()


def random_parametrs():
    types = ['POLAR', 'BROWN', 'BLACK', 'GUMMY']
    return {
        "bear_type": random.choice(types),
        "bear_name": faker.name(),
        "bear_age": random.uniform(-50,50)
    }
class Restful:

    sess = requests.session()
    host = None
    def __init__(self,host):
        self.host = host

    def create_new_bear(self,type,name,age):
        param = random_parametrs(type,name,age).param()
        return self.sess.post(self.host + '/bear', json=param)

    def read_all_bears(self):
        return self.sess.get(self.host + '/bear')

    def update_bear(self, bear_id, param):
        return self.sess.put(self.host + '/bear/' + str(bear_id), json=param)

    def read_bear(self,bear_id):
        return self.sess.get(self.host + '/bear/' + str(bear_id))

    def dell_bear(self,bear_id):
        return self.sess.delete(self.host + '/bear/' + str(bear_id))

    def dell_all_bear(self):
        return self.sess.delete(self.host + '/bear')

for i in range(10):
    print(random_parametrs())