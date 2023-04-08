"""
Author: Adrian Joost
created: April 2022
Notes:
Utilities functions for API Handler
"""

from flask import make_response, jsonify

def create_response (body, status):
    #creates an API-response object. Body should be json format.
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response