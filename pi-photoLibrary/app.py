import os
import platform

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models.photo import Photo

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('/googleCredentials/googleCredentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def check_posted_data(posted_data, required_fields):
    for field in required_fields:
        if field not in posted_data:
            return {'code': 301, 'message': f'Field named {field} not found in post.'}

    return {'code': 200}


class AddPhoto(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        required_fields = ['photoName']
        status_dict = check_posted_data(posted_data, required_fields)
        if status_dict['code'] != 200:
            ret_json = {
                "Message": status_dict['message'],
                "Status Code": str(status_dict['code'])
            }
            return jsonify(ret_json)

        name_of_photo = posted_data["photoName"]

        doc_ref = db.collection(u'photos').document(name_of_photo)
        doc_ref.set({
            u'pathToFile': f'/photos/{name_of_photo}.jpg',
        })

        ret_map = {
            'Message': 'cool',
            'Status Code': 200
        }
        return jsonify(ret_map)


class GetPhotos(Resource):
    def get(self):
        photos = os.listdir('/CF/DCIM/100EOS5D/')

        # collection_ref = db.collection(u'photos')
        # photos = collection_ref.stream()
        #
        # photos_found = []
        # for photo in photos:
        #     photos_found.append(photo.to_dict())

        ret_map = {
            'Message': photos,
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


api.add_resource(AddPhoto, "/addPhoto")
api.add_resource(GetPhotos, "/getPhotos")
api.add_resource(InitializeSession, "/initializeSession")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    if platform.system() == "Windows":
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
