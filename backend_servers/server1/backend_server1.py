from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<path:path>', methods=['GETS', 'POST', 'PUT', 'DELETE' ])
def handle_request(path):
    return jsonify({
        "message": "Response from server 1",
        "path": path,
        "method":request.method,
        "args": request.args,
        "json": request.json
    })

if __name__ == '__main__':
    app.run(port=5001)