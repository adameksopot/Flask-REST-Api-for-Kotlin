from flask import Flask
from flask_restful import Api
from location_values import LocationValues

app = Flask(__name__)
api = Api(app)
api.add_resource(LocationValues, '/adamapi')


@app.route('/')
def hello():
    return 'Hello,REST'


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True,port= 3000)