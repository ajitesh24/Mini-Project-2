import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("connectingfirebasedbtopy-d73a8-firebase-adminsdk-n6v1l-cf641b1d35.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://connectingfirebasedbtopy-d73a8-default-rtdb.firebaseio.com"
})

users_ref = db.reference()
users_ref.set({
    'ca0r099Count' : 1
})