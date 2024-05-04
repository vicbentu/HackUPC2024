from flask import Flask, jsonify, request
from flask_cors import CORS
from travelers import Travelers
from scheduler import Scheduler
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/getSchedule', methods=['GET'])
def get_schedule():
    city = request.args.get('city')
    print(request.args.get('depDate'))
    depDate = datetime.strptime(request.args.get('depDate'), '%Y-%m-%d')
    retDate = datetime.strptime(request.args.get('retDate'), '%Y-%m-%d')
    return jsonify(scheduler.getSchedule(city, depDate, retDate))
    
@app.route('/getAllGustos', methods=['GET'])
def get_all_gustos():
    return jsonify(travelers.get_all_gustos())

if __name__ == '__main__':
    travelers = Travelers()
    scheduler = Scheduler()
    app.run(debug=True, host='0.0.0.0', port=5000)
