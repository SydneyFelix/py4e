import random
import string

keys = ['id','username','password']
users = ['pong','ping']

data = [{key:(i if key=='id' else users[i] if key=='username' else "".join(random.choices(string.printable,k=12)))for key in keys} for i in range(len(users))]
for i in data:
    print(i)
