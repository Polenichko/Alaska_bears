# info
# Welcome to Alaska!
# This is CRUD service for bears in alaska.
# CRUD routes presented with REST naming notation:
# POST /bear - create
# GET /bear - read all bears
# GET /bear/:id -read specific bear
# PUT /bear/:id - update specific bear
# DELETE /bear - delete all bears
# DELETE /bear/:id - delete specific
# bear Example of ber json: {
# "bear_type":"BLACK",
# "bear_name":"mikhail",
# "bear_age":17.5}.
# Available types for bears are: POLAR, BROWN, BLACK and GUMMY.
import requests
import json


host = 'http://localhost:32768'

class Parametrs_bear:

    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

    def param(self):
        param_dict = {"bear_type": self.type, "bear_name": self.name, "bear_age": self.age}
        return param_dict

class Restful:

    sess = requests.session()
    host = None
    def __init__(self,host):
        self.host = host

    def create_new_bear(self,type,name,age):
        param = Parametrs_bear(type,name,age).param()
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

def jprint(obj):
    try:
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    except:
        print(obj)


print(Restful(host).read_all_bears().json())

# json = res.json()
# bear_id = json[0]['bear_id']
