# This code should be used with every script that you will be using to connect to the Firebase database.
import pyrebase
from firebase import firebase



config = {
  # You can get all these info from the firebase website. It's associated with your account.
  apiKey: "AIzaSyCIpsNHMEkUKqEiXpQVgiTRA95_WxeaIKg",
  authDomain: "distance-e9ce8.firebaseapp.com",
  databaseURL: "https://distance-e9ce8-default-rtdb.firebaseio.com",
  projectId: "distance-e9ce8",
  storageBucket: "distance-e9ce8.appspot.com",
  messagingSenderId: "814402079869",
  appId: "1:814402079869:web:ed1a246a04959fd12ab514"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
database = firebase.database()
a = 1
print(a)
database.child("DB object name")
data = {"key1": a}
database.set(data)
