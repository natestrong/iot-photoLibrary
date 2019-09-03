import os
import platform

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from models.photo import Photo

app = Flask(__name__)
api = Api(app)
CORS(app)

cred = credentials.Certificate('/googleCredentials/googleCredentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def check_posted_data(posted_data, required_fields):
    for field in required_fields:
        if field not in posted_data:
            return {'code': 301, 'message': f'Field named {field} not found in post.'}

    return {'code': 200}


class CurrentSessionCount(Resource):
    def get(self):
        photos = os.listdir('/CF/DCIM/100EOS5D/')

        photos_count = len(photos)

        ret_map = {
            'Message': photos_count,
            'Status Code': 200
        }
        return jsonify(ret_map)


class InitializeSession(Resource):
    def post(self):
        raw_photos = os.listdir('/CF/DCIM/100EOS5D/')

        collection_ref = db.collection(u'currentSession')

        batch = db.batch()

        for index, raw_photo in enumerate(raw_photos, start=1):
            print(f'processing {index} of {len(raw_photos)}')
            photo = Photo(os.path.splitext(raw_photo)[0], '8_31_19')

            photo_ref = collection_ref.document(photo.photo_id)
            batch.set(photo_ref, vars(photo))

        batch.commit()

        ret_map = {
            'Message': f'Uploaded {len(raw_photos)} photos',
            'Status Code': 200
        }
        return jsonify(ret_map)


api.add_resource(CurrentSessionCount, "/currentSessionCount")
api.add_resource(InitializeSession, "/initializeSession")


@app.route('/')
def hello_world():
    return "Hello World! Sent from Python!"


if __name__ == "__main__":
    if platform.system() == "Windows":
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
