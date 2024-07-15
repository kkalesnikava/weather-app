from app import app
from flask import jsonify


# Error handling
@app.errorhandler(404)
def not_found_error(error):
    response = {
        "message": "Resource not found",
        "status_code": 404
    }
    return jsonify(response), 404


@app.errorhandler(500)
def internal_error(error):
    response = {
        "message": "Internal Error, resouce unavailable",
        "status_code": 500
    }
    return jsonify(response), 500
