import platform

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('/googleCredentials/googleCredentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def checkPostedData(postedData, requiredFields):
    for field in requiredFields:
        if field not in postedData:
            return {'code': 301, 'message': f'Field named {field} not found in post.'}
        else:
            return {'code': 200}


class AddPhoto(Resource):
    def post(self):
        postedData = request.get_json()
        requiredFields = ['photoName']
        statusDict = checkPostedData(postedData, requiredFields)
        if (statusDict['code'] != 200):
            retJson = {
                "Message": statusDict['message'],
                "Status Code": str(statusDict['code'])
            }
            return jsonify(retJson)

        nameOfPhoto = postedData["photoName"]

        doc_ref = db.collection(u'photos').document(nameOfPhoto)
        doc_ref.set({
            u'pathToFile': f'/photos/{nameOfPhoto}.jpg',
        })

        retMap = {
            'Message': 'cool',
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(AddPhoto, "/addPhoto")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    if platform.system() == "Windows":
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
