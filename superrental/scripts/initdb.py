import sys, os
if os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','..')) not in sys.path:
    sys.path.append(os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','..')))

from superrental import app, mongo

rentals = [{
        "type": 'rentals',
        'id': 'grand-old-mansion',
        'attributes': {
          'title': 'Grand Old Mansion',
          'owner': 'Veruca Salt',
          'city': 'San Francisco',
          'type': 'Estate',
          'bedrooms': 15,
          'image': 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Crane_estate_(5).jpg'
        }
      }, {
        'type': 'rentals',
        'id': 'urban-living',
        'attributes': {
          'title': 'Urban Living',
          'owner': 'Mike Teavee',
          'city': 'Seattle',
          'type': 'Condo',
          'bedrooms': 1,
          'image': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Alfonso_13_Highrise_Tegucigalpa.jpg'
        }
      }, {
        'type': 'rentals',
        'id': 'downtown-charm',
        'attributes': {
          'title': 'Downtown Charm',
          'owner': 'Violet Beauregarde',
          'city': 'Portland',
          'type': 'Apartment',
          'bedrooms': 3,
          'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f7/Wheeldon_Apartment_Building_-_Portland_Oregon.jpg'
        }
      }]

def initdb():
    with app.app_context():
        mongo.db.rentals.insert_many(rentals)

if __name__ == '__main__':
    initdb()
