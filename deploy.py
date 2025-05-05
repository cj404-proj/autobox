import subprocess
import os

def deploy_flask_app():
    subprocess.run(["sudo", "apt-get", "install", "-y", "nginx", "python3-venv"], check=True)
    os.makedirs("/opt/flaskapp", exist_ok=True)
    with open("/opt/flaskapp/app.py", "w") as f:
        f.write('''from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return "Hello from Flask!"\nif __name__ == '__main__':\n    app.run(host='0.0.0.0')''')
    subprocess.run(["python3", "-m", "venv", "/opt/flaskapp/venv"], check=True)
    subprocess.run(["/opt/flaskapp/venv/bin/pip", "install", "flask"], check=True)
    with open("/etc/systemd/system/flaskapp.service", "w") as f:
        f.write('''[Unit]\nDescription=Flask App\nAfter=network.target\n\n[Service]\nUser=root\nWorkingDirectory=/opt/flaskapp\nExecStart=/opt/flaskapp/venv/bin/python app.py\nRestart=always\n\n[Install]\nWantedBy=multi-user.target''')
    subprocess.run(["sudo", "systemctl", "daemon-reexec"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "flaskapp"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "flaskapp"], check=True)
