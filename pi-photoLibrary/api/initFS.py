import firebase_admin
from firebase_admin import credentials, firestore


def initFS():
    print('FS initislized')
    cred = credentials.Certificate('/googleCredentials/googleCredentials.json')
    firebase_admin.initialize_app(cred)

    return firestore.client()
