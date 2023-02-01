import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate(r"D:\Github\0820GUI\firebase\userbase-a8b89-firebase-adminsdk-m7weo-80d894d357.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# #Get Collection
# col_ref = db.collection(u"User_name")

# docs = col_ref.stream()

# # for doc in docs:
#     # print(u'{} => {}'.format(doc.id, doc.to_dict()))
#     # print(doc.to_dict())
    
# #Get Doc
# doc_ref = db.collection("User_name").document('簡川隆')
# doc = doc_ref.get()

# print('姓名 => {}'.format(doc.to_dict()['姓名']))
# print('信箱 => {}'.format(doc.to_dict()['信箱']))
# print('電話 => {}'.format(doc.to_dict()['電話']))

#--------------
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:
    def __init__(self):
        self.cred = credentials.Certificate(r"firebase\userbase-a8b89-firebase-adminsdk-m7weo-80d894d357.json")
        
        self.app=firebase_admin.initialize_app(self.cred)
        db = firestore.client()
        self.users = list(db.collection(u'User_name').stream())

        users_dict = list(map(lambda x: x.to_dict(), self.users))
        self.df = pd.DataFrame(users_dict)
        firebase_admin.delete_app(self.app)
        self.a="123123"
    def ok(self):
        
        
        self.f="7777"
        print(self.f)
class Abs:
    def __init__(self):
        self.b=Firebase().df
        
    def abc(self):
        self.b=Firebase().df
        self.ppp=Firebase().ok()
        
        # print(self.a.df)
if __name__ == '__main__':
    a=Firebase().df
    print(a)


    