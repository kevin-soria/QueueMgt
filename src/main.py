"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Person, Queue
from send_sms import first_function

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/sendmsg', methods=['GET'])
def first_msg():

    first_function('Test')

    return jsonify({'msg':'message sent!' }), 200

@app.route('/newmsg', methods=['POST'])
def new_message():

    body = request.form()
    
    name = body['Body']
    number = body['From']
    message =  name + ", you are now in the queue."

    Queue().enqueue(name, number)
    
    resp = MessagingResponse()
    resp.message("Hello " + message_body + " you have been added."  " There are " + repr(len(Queue()._queeue)-1) + " person in front of you.")
    return  str(resp)

@app.route('/all_queue', methods=['GET'])
def getting_all_messages():
    return jsonify(Queue()._queue), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
