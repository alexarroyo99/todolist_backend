from flask import request,jsonify
from flask_restful import Resource,abort
from firestore_service import methods



class User(Resource):
    def get(self,id):
        users=methods.getUsers()
        for user in users:
            if id in user.id:
                username=id
                return jsonify(methods.getUser(username))
        return abort(400,"User doesnt exist")


    def post(self):
        user= request.form
        methods.insertUser(user)
        return 'User created'

    def put():
        user=request.form
        methods.updatePassword(user)

class UserTasks(User):
    def get():
        pass
    
    def post():
        pass

    def delete():
        pass



