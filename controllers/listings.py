from config.db import collection
from bson.json_util import dumps
from bson.objectid import ObjectId


class Items(object):
    def __init__(self):
        self.collection = collection

    def get_all_item(self):
        try:
            items = list(self.collection.find())
            return dumps({'success': True, 'data': items})
        except ValueError as e:
            return dumps({'error': str(e)})

    def get_item(self, id_):
        try:
            item = self.collection.find_one({'_id': ObjectId(id_)})
            return dumps({'success': True, 'data': item})
        except ValueError as e:
            return dumps({'error': str(e)})

    def update_item(self, obj):
        try:
            id_ = obj['_id']
            del obj['_id']
            self.collection.update_one({'_id': ObjectId(id_)}, {"$set": obj})
            return dumps({'success': True, 'data': obj})
        except ValueError as e:
            return dumps({'error': str(e)})

    def delete_item(self, id_):
        try:
            self.collection.delete_one({'_id': ObjectId(id_)})
            return dumps({'success': True})
        except ValueError as e:
            return dumps({'error': str(e)})
