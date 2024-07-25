from flask import request, jsonify
from src.handlers.abbreviations import answer

def handle_post():
  data = request.get_json()

  if not data:
    return jsonify({'error': 'Missing JSON data'}), 400

  response = {
    'no_abbr_message': answer(data["message"]),
    'received_data': data,
  }

  return jsonify(response), 200