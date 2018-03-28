'''mysqlclient
easy gui
file ->setting
http://mysqlclient.readthedocs.io/
http://blog.tecladocode.com/learn-python-encrypting-passwords-python-flask-and-passlib/
https://gist.github.com/adnanfajr/986a99d42516c743dadfa6e3c3d5c848
https://www.python-course.eu/python_tkinter.php
http://mysqlclient.readthedocs.io/user_guide.html#some-examples'''

from controller.Authentication import Authentication

user = Authentication().user

print(user)