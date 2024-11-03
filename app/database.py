import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
# Initialize Firebase using the service account key
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://teremfoglalas-faa5b-default-rtdb.europe-west1.firebasedatabase.app/"
        })
