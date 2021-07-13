from flask import Flask
from flask_restful import Api
from classes import User, UserTasks
from flask_cors import CORS

app= Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(User,'/user/<id>')
api.add_resource(UserTasks,'/user/<id>/tasks')

if __name__=='__main__':
    app.run(debug=True)

