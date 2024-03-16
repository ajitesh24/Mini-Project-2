# Write your code here :-)
import pyrebase
from distance import distance


config = {
  apiKey: "AIzaSyCIpsNHMEkUKqEiXpQVgiTRA95_WxeaIKg",
  authDomain: "distance-e9ce8.firebaseapp.com",
  databaseURL: "https://distance-e9ce8-default-rtdb.firebaseio.com",
  projectId: "distance-e9ce8",
  storageBucket: "distance-e9ce8.appspot.com",
  messagingSenderId: "814402079869",
  appId: "1:814402079869:web:ed1a246a04959fd12ab514"

};


firebase = pyrebase.initialize_app(config)



storage = firebase.storage()
database = firebase.database()
a = distance()
print(a)
database.child("DB object name")
data = {"key1": a}
database.set(data)







