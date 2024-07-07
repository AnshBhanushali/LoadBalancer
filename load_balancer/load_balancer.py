from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# These are the backend server the project would work on
backend_servers = [
    'http://localhost:5001',
    'http://localhost:5002'
]

current_server = 0

@app('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def load_balancer(path):
    global current_server
    backend_url = f"{backend_servers[current_server]}/{path}"

    # This pushes the incomming request to backend servers
    if request.method == 'GET':
        response = requests.get(backend_url, params=request.args)
    elif request.method == 'POST':
        response = requests.post(backend_url, json=request.json)
    elif request.method == 'PUT':
        response = requests.put(backend_url, json=request.json)
    elif request.method == 'DELETE':
        response = requests.delete(backend_url)
        