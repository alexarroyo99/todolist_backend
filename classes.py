import bcrypt
from flask import request,jsonify
from flask_restful import Resource,abort
from firestore_service import methods
import json



class User(Resource):
    def get(self):
        username=request.json['username']
        user=methods.getUser(username)
        if user == None:
            return jsonify(abort(404,messege='User or password invalid'))
        user_id=user['user_id']
        name=user['name']
        user_password=user['password']
        if bcrypt.checkpw(request.json['password'].encode('utf-8'),user_password):
            return jsonify({'user_id': user_id,'name':name})
        return jsonify(abort(404,messege='User or password invalid'))
        

    def post(self):
        user= request.json
        m=methods.insertUser(user)
        if m == None:
            return jsonify(abort(400,messege='User already exists'))
        return jsonify({'messege': 'User created'})


    def put(self):
        user=request.json
        methods.updatePassword(user)
        return jsonify({'messege':'Password updated'})

class UserTasks(Resource):
    def get(self):
        user_id=request.json['user_id']
        tasks=methods.getTasks(user_id)
        return jsonify(tasks)


    def post(self):
        user=request.json
        methods.insertTask(user)
        return jsonify({'messege':'Task added'})


    def delete(self):
        task_id=request.json['task_id']
        methods.deleteTask(task_id)
        return jsonify({'messege':'Task deleted'})


    def put(self):
        task_id=request.json['task_id']
        methods.updateTaskState(task_id)
        return jsonify({'messege':'Task status uptdated'})



