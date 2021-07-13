import firebase_admin
from firebase_admin import credentials,firestore

cred= credentials.Certificate('./todolist_credential.json')
firebase_admin.initialize_app(cred)

db=firestore.client()

class methods:
    def getUser(username):
        user = db.collection('users').document(username).get()
        return user.to_dict()

    def getTasks():
        pass

    def getUsers():
        users = db.collection('users').stream()
        return users

    def deleteTask():
        pass

    def updatePassword(user):
        db.collection('users').document(user['username']).update({'password': user['newpassword']})

    def updateTaskState():
        pass

    def insertUser(user):
        db.colletions('users').document(user['username']).set({'password':user['password'],'name':user['name']})

    def insertTask():
        pass









