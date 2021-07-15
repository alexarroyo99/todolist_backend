import firebase_admin
import bcrypt
from firebase_admin import credentials,firestore


cred= credentials.Certificate('./todolist_credential.json')
firebase_admin.initialize_app(cred)

db=firestore.client()

class methods:
    def getUser(username):
        user = db.collection('users').where('username','==',username).stream()
        if user == None:
            return user
        for u in user:
            return {'user_id':u.id,'password':u.to_dict()['password'],'name':u.to_dict()['name']}

    def getTasks(user_id):
        tasks=db.collection('tasks').where('user_id','==',user_id).stream()
        tasks_list={}
        n=0
        for t in tasks:
            n+=1
            a=t.to_dict()
            a['task_id']=t.id
            a.pop('user_id')
            tasks_list[str(n)]=a
        return tasks_list


    def deleteTask(task_id):
        db.collection('tasks').document(task_id).delete()


    def updatePassword(user):
        db.collection('users').document(user['user_id']).update({'password': user['newpassword']})


    def updateTaskState(task_id):
        task=db.collection('tasks').document(task_id).get()
        if task.to_dict()['status']=='pending':
            return db.collection('tasks').document(task_id).update({'status': 'done'})
        return db.collection('tasks').document(task_id).update({'status': 'pending'})




    def insertUser(user):
        doc=db.collection('users').where('username','==',user['username']).get()
        hashed_password=bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt())
        user['password']= hashed_password
        if len(doc)==0:
            return db.collection('users').add({'username':user['username'],'password':user['password'],'name':user['name']})
        return None


    def insertTask(user):
        db.collection('tasks').add({'user_id':user['user_id'],'description':user['description'],'status':'pending'})
        

        









