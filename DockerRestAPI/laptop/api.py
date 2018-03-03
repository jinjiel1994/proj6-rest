# Laptop Service
import flask
import pymongo
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


client = MongoClient('db', 27017)
db = client.time


class listAll(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]

        return {'km': [item['km'] for item in items],
                'open': [item["open"] for item in items],
                'close': [item["close"] for item in items]
                }


class listOpenOnly(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]

        return {'open': [item["open"] for item in items]
                }


class listCloseOnly(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]

        return {'close': [item["close"] for item in items]
                }


class listAllcsv(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]
        csv = 'open, close\n'
        for item in items:
            csv += '%s, %s\n' % (item['open'], item['close'])
        csv = csv.strip('\n')
        csv = csv.split('\n')
        return csv


class listOpenOnlycsv(Resource):
    def get(self):

        top = flask.request.args.get("top", type=int)
        if top is None:
            _items = db.time.find()
        else:
            _items = db.time.find().sort("open", pymongo.ASCENDING).limit(top)

        items = [item for item in _items]
        csv = 'open\n'
        for item in items:
            csv += '%s\n' % item['open']
        csv = csv.strip('\n')
        csv = csv.split('\n')
        return csv


class listCloseOnlycsv(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]
        csv = 'close\n'
        for item in items:
            csv += '%s\n' % item['close']
        csv = csv.strip('\n')
        csv = csv.split('\n')
        return csv


class listAlljson(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]
        json = []
        for item in items:
            json.append({'km': item['km'],
                'open': item['open'],
                'close': item['close']
                })
        return json


class listOpenOnlyjson(Resource):
    def get(self):
        top = flask.request.args.get("top", type=int)
        if top is None:
            _items = db.time.find()
        else:
            _items = db.time.find().sort("open", pymongo.ASCENDING).limit(top)

        items = [item for item in _items]
        json = []
        for item in items:
            json.append({'km': item['km'],
                         'open': item['open']
                        })
        return json


class listCloseOnlyjson(Resource):
    def get(self):
        _items = db.time.find()
        items = [item for item in _items]
        json = []
        for item in items:
            json.append({'km': item['km'],
                         'close': item['close']
                        })
        return json


# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll')
api.add_resource(listOpenOnly, '/listOpenOnly')
api.add_resource(listCloseOnly, '/listCloseOnly')
api.add_resource(listAllcsv, '/listAll/csv')
api.add_resource(listOpenOnlycsv, '/listOpenOnly/csv')
api.add_resource(listCloseOnlycsv, '/listCloseOnly/csv')
api.add_resource(listAlljson, '/listAll/json')
api.add_resource(listOpenOnlyjson, '/listOpenOnly/json')
api.add_resource(listCloseOnlyjson, '/listCloseOnly/json')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
