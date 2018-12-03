import sqlite3
import json
import urllib.parse
import requests
from platform import system as system_name
from subprocess import call as system_call

host = 'https://pms.kmm-vsu.ru/'
host_for_ping = 'pms.kmm-vsu.ru'
email = 'pacan@1337.ru'
pwd = '12345679'


class API:
    def __init__(self):
        self.token = ''
        self.user = ''
        self.pwd = ''


    def authorization(self, email, pwd):
        data = json.dumps({"requests": {"authorization": {"email": email, "pwd": pwd}}, 'token': ''})
        response = requests.post(host, data=data).json()
        self.token = response['content']['authorization']['content']
        return response['content']['authorization']['ok']


    def send_query(self, args):
        data = json.dumps({"requests": args, 'token': self.token})
        response = requests.post(host, data=data).json()
        try:
            if response['error_code'] == 403:
                self.authorization(self.user, self.pwd)
                data = json.dumps({"requests": args, 'token': self.token})
                response = requests.post(host, data=data).json()
        except Exception:
            pass
        if not (len(args) == 1):
            pass
        elif response['ok']:
            try:
                return tuple(response['content'].values())[0]['content']
            except Exception:
                pass
        return response


    def ping_server(self):
        param = '-n' if system_name().lower()=='windows' else '-c'
        command = ['ping', param, '1', host_for_ping]
        return system_call(command) == 0


    def get_all_users(self):
        return self.send_query({"get_all_users": {}})


    def get_all_projects(self):
        return self.send_query({"get_all_projects": {}})


    def add_users(self, users):
        return self.send_query({"add_users": users})


    def edit_users(self, users):
        return self.send_query({"edit_users": users})


    def del_users(self, email):
        return self.send_query({"del_users": email})


    # def edit_user(self, email, pwd, surname, name, patronymic, position):
    #     return self.send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'edit_user')


    def add_project(self, name, deadline):
        return self.send_query({"add_projects": [
            {'name': name, 'deadline': deadline}
        ]})


    # def edit_project(self, token, name, deadline):
    #     return

    # def get_users_projects(self, ):
    #     return self.send_query({}, 'get_users_projects')

    # def get_all_projects(self):
    #     return self.send_query({}, 'get_all_projects')