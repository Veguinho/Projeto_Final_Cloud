import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["tarefa"]

myclient.mydb.add_user('veguinho', 'vegs123', roles=[{'role':'readWrite','db':'tarefa'}])

mycol = mydb["tarefas"]

mydict = { "nome": "Tarefa 0", "dificuldade": 0 }

tarefa0 = mycol.insert_one(mydict)