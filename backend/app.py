from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

# Initialize Flask-RESTx API
api = Api(app, version='1.0', title='Sample API', description='A simple API with Swagger documentation')

# Namespace for the API
ns = api.namespace('hello', description='Hello World operations')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """Returns a simple 'Hello, World!' message."""
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
