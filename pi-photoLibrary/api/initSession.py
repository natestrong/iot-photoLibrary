import os
import time

import firebase_admin
from firebase_admin import firestore
from flask import jsonify, request
from flask_restful import Resource

from .initFS import initFS
from .models.fscollection import FSCollection
from .models.photo import Photo


class InitializeSession(Resource):
    def __init__(self):
        self.__name__ = __name__
        if not firebase_admin._apps:
            self.db = initFS()
        else:
            self.db = firestore.client()

        self.photo_dir = '/CF/DCIM/100EOS5D/'
        self.raw_photos = os.listdir(self.photo_dir)

        self.collection_ref = self.db.collection(u'currentSession')

        self.fs_photos = FSCollection(self.collection_ref)

    def post(self):
        posted_data = request.get_json()
        print(posted_data)

        total_deleted = None
        if posted_data['deleteFirst']:
            print('Deleting existing collection:')
            total_deleted = self.fs_photos.delete_collection()
            print(f'Deleted: {total_deleted}')

        self.prune_existing_photos()

        self.update_collection()

        self.update_thumbnails()

        message = ''
        if total_deleted:
            message += f'Deleted {str(total_deleted)}. '

        message += f'Uploaded {len(self.raw_photos)} photos. '

        ret_map = {
            'Message': message,
            'Status Code': 200
        }
        print('Finished')
        return jsonify(ret_map)

    def prune_existing_photos(self):
        docs = self.fs_photos.get_docs()
        for index, doc in enumerate(docs, start=1):
            doc_dict = doc.to_dict()
            property_list = ['thumbnail_blob',
                             'filepath_jpeg',
                             'filepath_thumbnail',
                             'photo_id',
                             'name',
                             'filepath_raw',
                             'date']

            photo_need_update = False
            for property in property_list:
                if property not in doc_dict:
                    photo_need_update = True

            if not doc_dict['thumbnail_blob']:
                photo_need_update = True

            if not photo_need_update:
                # Photo does not need to be updated. Remove it from self.raw_photos
                self.raw_photos.remove(doc_dict['name'])

    def update_collection(self):
        batch = self.db.batch()

        for index, raw_photo in enumerate(self.raw_photos, start=1):
            print(f'processing {index} of {len(self.raw_photos)}')

            filepath = os.path.join(self.photo_dir, raw_photo)
            date_string = time.strftime('%Y-%m-%d', time.localtime(os.path.getctime(filepath)))

            photo = Photo(raw_photo, date_string, self.photo_dir)

            photo_ref = self.collection_ref.document(photo.photo_id)
            batch.set(photo_ref, vars(photo))

        batch.commit()

    def update_thumbnails(self):
        docs = self.fs_photos.get_docs()
        batch = self.db.batch()
        for index, doc in enumerate(docs, start=1):
            doc_dict = doc.to_dict()
            photo = Photo(**doc_dict)
            print(f'Processing thumbnail for: {photo.photo_id}')

            photo.create_thumbnail()

            photo_ref = self.collection_ref.document(photo.photo_id)
            batch.set(photo_ref, vars(photo))

        batch.commit()
