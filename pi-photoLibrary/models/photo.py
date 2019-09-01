class Photo:
    def __init__(self, name, date, photo_id=None):
        self.name = name
        self.date = date

        if photo_id:
            self.photo_id = photo_id
        else:
            self.photo_id = self.generate_photo_id()

    def generate_photo_id(self):
        return self.name + self.date
