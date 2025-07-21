from flask import Flask, request, jsonify
import socket

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
    app.run(host='127.0.0.1', port=8080, debug=True)
