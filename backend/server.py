from flask import Flask, jsonify, request
from flask_cors import CORS
from travelers import Travelers

app = Flask(__name__)
CORS(app)

@app.route('/getPlan', methods=['GET'])
def get_information():
    
    return jsonify({"message": "This is a GET request, returning static information."})

@app.route('/getAllGustos', methods=['GET'])
def get_all_gustos():
    return jsonify(travelers.get_all_gustos())

if __name__ == '__main__':
    travelers = Travelers()
    app.run(debug=True, port=5000)
