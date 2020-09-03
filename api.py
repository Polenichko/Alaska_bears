import requests

class Restful:

    sess = requests.session()
    host = None

    def __init__(self,host):
        self.host = host

    def create_new_bear(self, param):
        return self.sess.post(self.host + '/bear', json=param)

    def read_all_bears(self):
        return self.sess.get(self.host + '/bear')

    def update_bear(self, bear_id, param):
        return self.sess.put(self.host + '/bear/' + str(bear_id), json=param)

    def read_bear(self, bear_id):
        return self.sess.get(self.host + '/bear/' + str(bear_id))

    def dell_bear(self, bear_id):
        return self.sess.delete(self.host + '/bear/' + str(bear_id))

    def dell_all_bear(self):
        return self.sess.delete(self.host + '/bear')
