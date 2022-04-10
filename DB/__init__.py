import pyrebase

# Configuration
config = {
  "apiKey": "AIzaSyADa4fhetZo3ppVEaFj1-1IuyTEtIqqyZc",
  "authDomain": "task-management-9bc8a.firebaseapp.com",
  "databaseURL": "https://task-management-9bc8a-default-rtdb.firebaseio.com",
  "projectId": "task-management-9bc8a",
  "storageBucket": "task-management-9bc8a.appspot.com",
  "messagingSenderId": "312135534778",
  "appId": "1:312135534778:web:d468c2472def5bb8125a83",
  "measurementId": "G-HE2VKCJKKB"
}

# Initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
