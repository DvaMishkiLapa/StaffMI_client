import urllib.parse
import requests
host = 'https://pms.kmm-vsu.ru/'

TOKEN = ''

email = 'admin@admin.ru'
pwd = '12345'


def send_query(args, act):
    global TOKEN
    args['token'] = TOKEN 
    url = host + act + '?' + urllib.parse.urlencode(args)
    response = requests.get(url)
    if "error" in response:
        TOKEN = auth(email, pwd)
        return requests.get(url).json()
    return response.json()


def auth(email, pwd):
    args = {'email': email, 'pwd': pwd}
    response = requests.get(host + 'auth?' + urllib.parse.urlencode(args)).json()
    try:
        return response['response']['token']
    except KeyError:
        return response['error']['error_msg']


def add_user(email, pwd, surname, name, patronymic, position):
    return send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'add_user')


def del_user(email):
    return send_query({'email': email}, 'del_user')


def edit_user(email, pwd, surname, name, patronymic, position):
    return send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'edit_user')


def get_all_users():
    return send_query({}, 'get_all_users')


def add_project(name, deadline):
    return


def del_project(token, name,):
    return


def edit_project(token, name, deadline):
    return

def get_users_projects():
    return send_query({}, 'get_users_projects')

def get_all_projects():
    return send_query({}, 'get_all_projects')

TOKEN = auth(email, pwd)
print(TOKEN)

for x in range(2):
    x = str(x+x)
    add_user(x + 'rulbor@ya.ru', x + 'rubot', x, x, x, x)

# print(del_user('user@user.ru'))
# print(edit_user('123@ya.ru', '', '', '', '', 'Ololoshkos'))

# print(get_all_projects())
# print(get_all_users())
# print(get_users_projects())