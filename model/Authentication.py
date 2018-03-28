from db import db
from encrypt import encrypt as crypt
class Authentication:
    user = {
        'username': '',
        'password': '',
        'email': ''
    }
    login = {
        'id': '',
        'username': '',
        'password': '',
        'email': ''
    }
    column = ['username', 'id', 'password','email']
    table = 'cred'
    conn = {}
    def __init__(self, user):
        self.user = user
        self.conn = db(self.table)
    def save(self):
        # self.user['password'] = crypt.crypt(self.user['password'])
        self.user['password'] = crypt.hash(self.user['password'],self.user['username'])
        ret = self.conn.insert(self.user)
        return ret
    def login(self):
        self.conn.where({'username=':self.user['username']})
        data = self.conn.select(self.column)
        if len(data['data']) > 0:
            user = data['data'][0]
            validate = self.validate(user)
            if validate:
                self.login = user
            return validate
        else:
            return 0
    def validate(self,user):
        return crypt.verify(self.user['password'], user['password'], user['username'])
    def user(self):
        return self.user
