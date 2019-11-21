from flask import Flask
from flask_restful import Api, Resource, reqparse
import os, pymongo, json

from bson import Binary, Code
from bson.json_util import dumps, RELAXED_JSON_OPTIONS

app = Flask(__name__)
api = Api(app)

mongodb_host = os.getenv('MONGODB_HOST', None)

myclient = pymongo.MongoClient("mongodb://{}:27017/".format(str(mongodb_host)))

mydb = myclient["tarefa"]

mycol = mydb["tarefas"]

class Tarefa():
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

tarefa0 = Tarefa("Tarefa 0", 0)

tarefas_dic = {0:{"nome":tarefa0.nome, "dificuldade":tarefa0.dificuldade}}

parser = reqparse.RequestParser()
parser.add_argument('tarefa')

class Req_noid(Resource):
    def get(self):
        data = {}
        data['lista'] = []
        cursor = mycol.find({})
        for document in cursor:
            print(document)
            data['lista'].append(str(document))
        json_data = json.dumps(data)
        return json_data, 200

    def post(self):
        index = 1
        # tarefas_dic[index] = {"nome":"Tarefa {}".format(index), "dificuldade":0}
        mydict = { "nome": "Tarefa {}".format(str(index)), "dificuldade": 0 }
        mycol.insert_one(mydict)
        return str(mycol[index]), 201

class Req_withid(Resource):
    def get(self, tarefa_id):
        if tarefa_id > len(tarefas_dic)-1:
            return 404
        else:
            return {tarefa_id: tarefas_dic[tarefa_id]}

    def put(self, tarefa_id):
        tarefas_dic[tarefa_id]["dificuldade"] += 1 
        return tarefas_dic[tarefa_id]

    def delete(self, tarefa_id):
        del tarefas_dic[tarefa_id]
        return tarefas_dic

class Healthcheck(Resource):
    def get(self):
        return 200

api.add_resource(Req_noid, '/Tarefa/')
api.add_resource(Req_withid, '/Tarefa/<int:tarefa_id>')
api.add_resource(Healthcheck, '/healthcheck/')
if __name__ == '__main__':
    #app.run(host="0.0.0.0",debug=True)
    app.run(host = os.getenv('LISTEN','0.0.0.0'), port=int(os.getenv('PORT','5000')),debug=True)