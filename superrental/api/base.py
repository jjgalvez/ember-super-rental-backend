from superrental import app, mongo
from superrental.lib import rental

from flask.json import jsonify
from flask import request

@app.route('/api/rentals', methods=['GET'])
def rentals():
    if request.method == 'GET' and not request.values.get('city', False):
        rentals = [rental(x) for x in mongo.db.rentals.find()]
        return jsonify( dict(data=rentals) )
    elif request.method == 'GET' and request.values.get('city'):
        city = request.values.get('city').lower().strip()
        print(city)
        rentals = [rental(x) for x in mongo.db.rentals.find({
                                'attributes.city': {'$regex': '^{}'.format(request.values.get('city').lower().strip()),
                                        '$options': 'i'}
                                })]
        return jsonify(dict(data=rentals))
    else:
        return dict(data=[])
