from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/getPlan', methods=['GET'])
def get_information():
    
    return jsonify({"message": "This is a GET request, returning static information."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)