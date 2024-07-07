from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# These are the backend server the project would work on
backended_servers = [
    'http://localhost:5001',
    'http://localhost:5002'
]

current_server = 0