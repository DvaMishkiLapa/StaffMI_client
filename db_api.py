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
        try:
            response = requests.post(host, data=data).json()
        except requests.exceptions.ConnectionError:
            pass
        self.token = response['content']['authorization']['content']
        return response['content']['authorization']['ok']


    def send_query(self, args):
        data = json.dumps({"requests": args, 'token': self.token})
        response = requests.post(host, data=data).json()
        try:
            if response['error_code'] == 403:
                self.authorization(self.user, self.pwd)
                data = json.dumps({"requests": args, 'token': self.token})
                response = requests.post('qwe', data=data).json()
        except KeyError:  
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


    def get_all_users(self, args):
        return self.send_query({"get_all_users": args})


    def get_all_projects(self, args):
        return self.send_query({"get_all_projects": args})


    def add_users(self, users):
        return self.send_query({"add_users": users})


    def edit_users(self, users):
        return self.send_query({"edit_users": users})


    def del_users(self, emails):
        return self.send_query({"del_users": emails})


    def add_projects(self, projects):
        return self.send_query({"add_projects": projects})


    def edit_projects(self, projects):
        return self.send_query({"edit_projects": projects})


    def del_projects(self, projects):
        return self.send_query({"del_projects": projects})

    def change_password(self, args):
        return self.send_query({"change_password": args})


    # def get_users_projects(self, ):
    #     return self.send_query({}, 'get_users_projects')

    # def get_all_projects(self):
    #     return self.send_query({}, 'get_all_projects')