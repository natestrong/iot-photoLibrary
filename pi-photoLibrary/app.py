import os
import platform

from api import initSession
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
CORS(app)


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


api.add_resource(CurrentSessionCount, "/currentSessionCount")
api.add_resource(initSession.InitializeSession(), "/initializeSession")


@app.route('/')
def hello_world():
    return "Hello World! Sent from Python!"


if __name__ == "__main__":
    if platform.system() == "Windows":
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
