import sqlite3
import json
import urllib.parse
import requests

host = 'https://pms.kmm-vsu.ru/'
# email = 'pacan@1337.ru'
# pwd = '12345679'


class API:

    def __init__(self, email, pwd):
        self.token = ''
        # self.token = self.auth(email, pwd)
        args = {"authorization": {"email": email, "pwd": pwd}}


    # def get_content(self, response, method):
    #     return response['content'][method]['content']

    def authorization(self, email, pwd):
        args = {"authorization": {"email": email, "pwd": pwd}}
        data = {"requests": args, 'token': ''}
        data = json.dumps(data)
        response = requests.post(host, data=data)
        return response['content']['authorization']['content']


    def send_query(self, args):
        data = {"requests": args, 'token': self.token}
        data = json.dumps(data)
        print('Я (Артём) отправил:')
        print(data)
        print('--------------------------')
        response = requests.post(host, data=data)
        return response.json()


    def get_all_users(self):
        args = {"get_all_users": {}}
        users = self.send_query(args)
        print(users)
        return users


    def get_projects(self):
        projects = self.send_query({}, 'get_all_projects')
        result = []
        for x in projects['response']:
            t = (x['name'], x['deadline'])
            result.append(t)
        return result


    def add_user(self, email, pwd, surname, name, patronymic, position):
        return self.send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'add_user')


    def del_user(self, email):
        return self.send_query({'email': email}, 'del_user')


    def edit_user(self, email, pwd, surname, name, patronymic, position):
        return self.send_query({'email': email, 'pwd': pwd, 'surname': surname, 'name': name, 'patronymic': patronymic, 'position': position}, 'edit_user')


    def add_project(self, name, deadline):
        return


    def del_project(self, token, name,):
        return


    def edit_project(self, token, name, deadline):
        return

    def get_users_projects(self, ):
        return self.send_query({}, 'get_users_projects')

    def get_all_projects(self):
        return self.send_query({}, 'get_all_projects')


    # Old code

    def _query(self, arg):
        self.cursor.execute(arg)
        self.connect.commit()
        return self.cursor


    def get_current_projects(self, worker_id):
        return self._query("SELECT * FROM projects WHERE id IN (SELECT project_id FROM data WHERE data.worker_id='{}')".format(worker_id))


    def get_id_project(self, project_name):
        return self._query("SELECT id FROM projects WHERE name='{}'".format(project_name))


    def update_workers(self, worker_data):
        return self._query("UPDATE workers SET surname='{1}', name='{2}', patronymic='{3}', post='{4}' WHERE id='{0}'".format(*worker_data))


    def insert_workers(self, worker_data):
        try:
            return self._query("INSERT INTO workers VALUES ('{}', '{}', '{}', '{}', '{}')".format(*worker_data))
        except:
            return []


    def update_projects(self, project_data):
        return self._query("UPDATE projects SET name='{1}', deadline='{2}' WHERE id='{0}'".format(*project_data))


    def insert_data(self, project_data):
        if not list(self._query("SELECT * FROM data WHERE worker_id='{}' AND project_id='{}'".format(*project_data))):
            return self._query("INSERT INTO data VALUES ('{}', '{}')".format(*project_data))


    def insert_projects(self, project_data):
        try:
            return self._query("INSERT INTO projects VALUES ('{}', '{}', '{}')".format(*project_data))
        except:
            return []


    def del_inproject(self, project_id):
        return self._query("DELETE FROM data WHERE project_id='{}'".format(project_id))


api = API('pacan@1337.ru', '12345679')
api.get_all_users()