from flask import Flask
import subprocess
import socket

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET'])
def get_host():
    return socket.gethostname()

@app.route('/', methods=['POST'])
def do_fork():
    new_process()
    return '', 204

def new_process():
    subprocess.Popen(["python3", "stress_cpu.py"])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
