from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome! Go to /htop for system info.</h1>'

@app.route('/htop')
def htop():
    username = os.getenv('USER', 'default_username')
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    top_output = subprocess.getoutput('top -bn1')

    return f'''
    <p><strong>Name:</strong>Priyanka P</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <p><strong>TOP output</strong></p>
    <pre>{top_output}</pre>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
