import getpass
from easygui import passwordbox
import re
from model.Authentication import Authentication as model
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
class Authentication:
    user ={
        'username': '',
        'password': '',
        'email': ''
    }
    register = ['email', 'username', 'password']
    login = ['username/email', 'password']
    def __init__(self):
        print("Welcome to PINK!")
        self.decision()
    def decision(self):
        access = ['Register', 'Login', 'Exit']
        print("Please type if [Register] to Register or [Login] to Login!")
        decision = input("What you want?")
        if(decision in access):
            getattr(self, '%s' % decision)()
        else:
            self.decision()
        return self.user
    def Exit(self):
        exit(200)
    def Register(self):
        print("Register")
        [self.set(cred) for cred in self.register]
        auth = model(self.user)
        ret = auth.save()
        if ret['success']:
            print('Registered!')
            Authentication()
        else:
            print("Can't save")

    def set(self, var):
        # self.user['email'] = input("Email: ")
        # self.user['username'] = input("Username: ")
        # try:
        #     self.user['password'] = getpass.getpass("Password: ", sys.stderr)
        # except getpass.GetPassWarning:
        #     print("Your system is not allowing us to disable echo. We cannot read your password")
        #     return
        # self.user['password'] = passwordbox("PASSWORD:")
        inpt = {
            'username': "Username: ",
            'username/email': "Username/Email: ",
            'password': "Password:",
            'email': "Email: "
        }
        self.user['username' if var == 'username/email' else var] = input(inpt[var]) if var != 'password' else passwordbox(inpt[var])
        self.validate(var)

    def Login(self):
        print("Login")
        [self.set(cred) for cred in self.login]
        auth = model(self.user)
        ret = auth.login()
        if ret:
            print("Welcome, ",self.user['username'])
        else:
            print("Invalid Credentials")
            [self.set(cred) for cred in self.login]


    def validate(self, var):
        name = 'username' if var == 'username/email' else var
        if (var =='email' and not EMAIL_REGEX.match(self.user['email'])) or (self.user[name] == '' or len(self.user[name]) < 3):
            print("invalid", var)
            self.set(var)