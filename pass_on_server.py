from flask import Flask
from flask_restful import Api, Resource, reqparse
import os, pymongo, json, requests

from bson import Binary, Code
from bson.json_util import dumps, RELAXED_JSON_OPTIONS

app = Flask(__name__)
api = Api(app)

pass_to_host = os.getenv('PASS_TO_HOST', None)

adress = "{}:5000/".format(str(pass_to_host))

class Req_noid(Resource):
    def get(self):
        r = requests.get(adress + '/Tarefa/')
        print("Status " + str(r.status_code))
        print(r.json())
        return r, 200

    def post(self):
        r = requests.post(adress + '/Tarefa/')
        print("Status " + str(r.status_code))
        print(r.json())
        return r, 201

# class Req_withid(Resource):
#     def get(self, tarefa_id):
#         if tarefa_id > len(tarefas_dic)-1:
#             return 404
#         else:
#             return {tarefa_id: tarefas_dic[tarefa_id]}

#     def put(self, tarefa_id):
#         tarefas_dic[tarefa_id]["dificuldade"] += 1 
#         return tarefas_dic[tarefa_id]

#     def delete(self, tarefa_id):
#         del tarefas_dic[tarefa_id]
#         return tarefas_dic

# class Healthcheck(Resource):
#     def get(self):
#         return 200

api.add_resource(Req_noid, '/Tarefa/')
# api.add_resource(Req_withid, '/Tarefa/<int:tarefa_id>')
# api.add_resource(Healthcheck, '/healthcheck/')
if __name__ == '__main__':
    app.run(host = os.getenv('LISTEN','0.0.0.0'), port=int(os.getenv('PORT','5000')),debug=True)