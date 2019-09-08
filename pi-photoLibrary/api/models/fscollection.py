class FSCollection:
    def __init__(self, coll_ref, batch_size=500):
        self.total_deleted = 0
        self.coll_ref = coll_ref
        self.batch_size = batch_size

    def delete_collection(self):
        docs = self.coll_ref.limit(self.batch_size).get()
        deleted = 0

        for doc in docs:
            print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()
            deleted += 1
            self.total_deleted += 1

        if deleted >= self.batch_size:
            return self.delete_collection()

        ret = self.total_deleted
        self.total_deleted = 0
        return ret

    def print_collection(self):
        docs = self.coll_ref.get()
        for doc in docs:
            print(f'{doc.id}')

    def get_docs(self, fs_filter=None):
        if fs_filter:
            return self.coll_ref.where(filter).get()

        return self.coll_ref.get()
