from flask import (Flask, request, render_template)
from flask_log_request_id import (RequestID, current_request_id)


APP = Flask(__name__)

@APP.route("/healthcheck")
def healthcheck():
    return 'OK'