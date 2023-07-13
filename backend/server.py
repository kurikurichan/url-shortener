import time

from flask import Flask, request, redirect
from flask_restful import Api, Resource, reqparse, abort
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
import hashlib
import base64
app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Url Shortener"
    },
)
def generate_unique_string(url):
    # Calculate the SHA-256 hash of the URL
    hash_object = hashlib.sha256(url.encode())
    hash_digest = hash_object.digest()

    # Encode the hash into a shorter representation (Base64 or hexadecimal)
    encoded_hash = base64.b64encode(hash_digest)[:6].decode()
    # Alternatively, you can use hexadecimal encoding:
    #encoded_hash = hash_object.hexdigest()[:6]

    return encoded_hash

url_dict = {}

class URLMapping(Resource):

    def get(self, key):
        if key not in url_dict:
            return {'message':'URL not found'}, 404
        # Set the Location header manually
        location = url_dict[key]['long_url']
        response = app.response_class(
            response='',
            status=302,
            headers={'Location': location}
        )
        return response

    def post(self, url):
        key = generate_unique_string(url)
        # Check if we already have that key in our system
        if key in url_dict:
            # We should  check to see if the url is the same as the duplicate key
            check_url = url_dict[key]['long_url']
            if check_url == url:
                url_dict[key]['message'] = 'Already created'
                # 409 return codes seems best for duplicate
                return url_dict[key], 409
            else:
                # TODO: Revisit how we create a unique key if Hash function returns same key for diff urls.
                key = str(time.time()).replace('.', '')[-6:]

        url_info = {'long_url': url,
                    'short_url': 'http://127.0.0.1:5000/url/' + key,
                    'key': key}

        url_dict[key]= url_info

        return url_dict[key], 201

    # TODO: need to complete
    def delete(self, key):
        return '', 204

    def get_urls(self):
        return url_dict, 200

api = URLMapping()

@app.route('/url', methods=['POST'])
def get_post():
    data = request.json  # Access JSON payload
    if not data.get('url'):
        return {'Missing field': 'url'}, 400
    else:
        url = data.get('url')
        return api.post(url)

@app.route('/url/<string:key>', methods=['GET'])
def return_get(key):
    return api.get(key)

@app.route('/urls', methods=['GET'])
def return_urls():
    return api.get_urls()

# Curl commmands to use
# curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.baeldung.com/curl-rest"}' http://127.0.0.1:5000/url -i
# curl http://127.0.0.1:5000/url/mEx0Mp -i
# To see the relocation header work add the -L option

if __name__ == '__main__':
    app.register_blueprint(swaggerui_blueprint)
    app.run(debug=True, port=5000)
