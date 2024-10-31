import firebase_admin
from  firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://teremfoglalas-faa5b-default-rtdb.europe-west1.firebasedatabase.app/"})

users_ref = db.reference("/Users")

new_user = {
    "id" : 123,
    "name" : "John Doe",
    "email" : "john.doe@example.com",
    "position" : "Engineer",
    "year" : 2022
}

users_ref.push(new_user)
all_users = users_ref.get()
print(all_users)