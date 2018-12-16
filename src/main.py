from flask import (Flask, request, render_template)
from flask_log_request_id import (RequestID, current_request_id)
from flask import jsonify

from aibici import AIBici


APP = Flask(__name__)

@APP.route('/a2b', methods=['POST'])
def a_to_b():
    origin = request.form['origin']
    destination = request.form['destination']

    aib = AIBici()
    loc_origin = aib.from_address(origin)
    loc_destination = aib.from_address(destination)

    result = aib.bicycle_a_to_b(loc_origin, loc_destination)
    return jsonify(result)

@APP.route("/healthcheck")
def healthcheck():
    return 'OK'
