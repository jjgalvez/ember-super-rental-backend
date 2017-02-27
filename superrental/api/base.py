from superrental import app, mongo
from superrental.lib import rental

from flask.json import jsonify
from flask import request

@app.route('/api/rentals', methods=['GET'])
@app.route('/api/rentals/<id>', methods=['GET'])
def rentals(id=False):
    if request.method == 'GET' \
        and not request.values.get('city', False) \
        and not id:
        rentals = [rental(x) for x in mongo.db.rentals.find()]
        return jsonify( dict(data=rentals) )
    elif request.method == 'GET' and request.values.get('city') \
        and not id:
        city = request.values.get('city').lower().strip()
        print(city)
        rentals = [rental(x) for x in mongo.db.rentals.find({
                                'attributes.city': {'$regex': '^{}'.format(request.values.get('city').lower().strip()),
                                        '$options': 'i'}
                                })]
        return jsonify(dict(data=rentals))
    elif request.method == 'GET' and \
        not request.values.get('city', False) and \
        id:
        rentalInfo = mongo.db.rentals.find_one_or_404(dict(id=id))
        return jsonify(dict(data=rental(rentalInfo)))
    else:
        return dict(data=[])
