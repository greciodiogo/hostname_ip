from flask import Flask, request, jsonify
import socket
import os

app = Flask(__name__)

def get_client_ip():
    return request.headers.get('X-Forwarded-For', request.remote_addr)

def get_client_hostname():
    ip = get_client_ip()
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

@app.route('/')
def get_client_info():
    ip = get_client_ip()
    hostname = get_client_hostname()
    return jsonify({"Hostname": hostname, "IP": ip})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
