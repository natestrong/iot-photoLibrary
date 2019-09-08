import os

import imageio as imageio
import rawpy
from PIL import Image


class Photo:
    def __init__(self, name, date, directory=None, photo_id=None, filepath_raw=None,
                 filepath_jpeg=None, filepath_thumbnail=None, thumbnail_blob=None):
        self.name = name
        self.date = date
        self.photo_id = photo_id if photo_id else self.generate_photo_id()
        self.filepath_raw = filepath_raw if filepath_raw else os.path.join(directory, name)
        self.filepath_jpeg = filepath_jpeg
        self.filepath_thumbnail = filepath_thumbnail
        self.thumbnail_blob = thumbnail_blob

    def generate_photo_id(self):
        return f'{self.date}_{os.path.splitext(self.name)[0]}'

    def create_thumbnail(self, size=300):
        self.filepath_jpeg = f'/photos/jpegs/{self.photo_id}.jpeg'

        if not os.path.exists(self.filepath_jpeg):
            raw = rawpy.imread(self.filepath_raw)
            rgb = raw.postprocess()
            imageio.imsave(f'/photos/jpegs/{self.photo_id}.jpeg', rgb)

        self.filepath_thumbnail = f'/photos/thumbnails/{self.photo_id}.jpeg'
        if not os.path.exists(self.filepath_thumbnail):
            image = Image.open(self.filepath_jpeg)
            image.thumbnail((size, size))
            image.save(self.filepath_thumbnail, 'JPEG')

        with open(self.filepath_thumbnail, "rb") as imageFile:
            self.thumbnail_blob = imageFile.read()
