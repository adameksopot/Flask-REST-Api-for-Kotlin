import sqlite3
from math import radians

from flask_restful import reqparse, Resource

from calculateDistance import calculateDistance


class LocationValues(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'latitude',
        type=float,
        required=True,
        help="You must enter latitude"
    )

    parser.add_argument(
        'longitude',
        type=float,
        required=True,
        help="You must enter longitude"
    )

    def get(self):
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = "select * from (select * from location order by id ASC LIMIT 1) UNION select * from (select * from location order by id DESC LIMIT 1)"

        result = cursor.execute(query).fetchmany(2)
        if result:
            connection.close()
            starting_point = result[0]
            ending_point = result[1]
            lat1 = starting_point[1]
            lon1 = starting_point[2]
            lat2 = ending_point[1]
            lon2 = ending_point[2]

            distance = calculateDistance(radians(lat1), radians(lon1), radians(lat2), radians(lon2))

            return {"Distance": round(distance, 2)}, 201
        return {"message": "failure"}, 400

    def post(self):
        data = LocationValues.parser.parse_args()
        item = {'latitude': data['latitude'], 'longitude': data['longitude']}
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = "INSERT INTO location VALUES(NULL ,?,?)"
        result = cursor.execute(query, (item['latitude'], item['longitude']))
        connection.commit()
        connection.close()
        if result:
            return {"message": "Posted with success"}, 201
