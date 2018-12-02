import sqlite3
import json
import urllib.parse
import requests

host = 'https://pms.kmm-vsu.ru/'
email = 'pacan@1337.ru'
pwd = '12345679'


class API:
    def __init__(self):
        self.token = ''
        self.user = ''
        self.pwd = ''
# {'ok': False, 'content': 'Token expired!', 'error_code': 403}

    def authorization(self, email, pwd):
        args = {"authorization": {"email": email, "pwd": pwd}}
        data = {"requests": args, 'token': ''}
        data = json.dumps(data)
        response = requests.post(host, data=data)
        self.token = response.json()['content']['authorization']['content']
        return response.json()['content']['authorization']['ok']


    def send_query(self, args):
        data = {"requests": args, 'token': self.token}
        data = json.dumps(data)
        response = requests.post(host, data=data).json()
        try:
            if response['error_code'] == 403:
                self.authorization(self.user, self.pwd)
                data = {"requests": args, 'token': self.token}
                data = json.dumps(data)
                response = requests.post(host, data=data).json()
        except Exception:
            pass
        if len(args) == 1:
            if response['ok']:
                try:
                    return tuple(response['content'].values())[0]['content']
                except Exception:
                    pass
        return response


    def get_all_users(self):
        args = {"get_all_users": {}}
        return self.send_query(args)


    def get_all_projects(self):
        args = {"get_all_projects": {}}
        return self.send_query(args)


    def add_users(self, users):
        args = {"add_users": users}
        return self.send_query(args)


    def edit_users(self, users):
        args = {"edit_users": users}
        return self.send_query(args)


    # def del_user(self, email):
    #     return self.send_query({'email': email}, 'del_user')


    # def edit_user(self, email, pwd, surname, name, patronymic, position):
    #     return self.send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'edit_user')


    def add_project(self, name, deadline):
        args = {"add_projects": [
            {'name': name, 'deadline': deadline}
        ]}
        return self.send_query(args)


    # def edit_project(self, token, name, deadline):
    #     return

    # def get_users_projects(self, ):
    #     return self.send_query({}, 'get_users_projects')

    # def get_all_projects(self):
    #     return self.send_query({}, 'get_all_projects')