from flask import Flask, request, jsonify
import socket
import os

app = Flask(__name__)

def get_client_hostname():
    return socket.gethostname()

def get_client_ip():
    return request.remote_addr

@app.route('/')
def get_client_info():
    hostname = get_client_hostname()
    ip = get_client_ip()
    return jsonify({"Hostname": hostname, "IP": ip})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
