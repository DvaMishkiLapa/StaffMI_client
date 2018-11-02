import json

f = open('memory.json', 'r')
data = json.loads(f.read())
f.close()

user = data['user_info']['login']
pwd = data['user_info']['pwd']
flag = data['flag']
print(pwd)
print(user)
print(flag)