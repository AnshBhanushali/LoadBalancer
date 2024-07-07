from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def handle_request(path):
    return jsonify({
        "message": "Response from server 2",
        "path": path,
        "method": request.method,
        "args": request.args,
        "json": request.json,
    })