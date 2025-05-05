# autobox.py
import argparse
from installer import install_packages
from user_manager import create_user
from config_editor import set_hostname
from deploy import deploy_flask_app
from logger import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description='AutoBox: Infrastructure Bootstrapper')
    parser.add_argument('--hostname', help='Set system hostname')
    parser.add_argument('--user', help='Create a system user')
    parser.add_argument('--install', nargs='+', help='Packages to install')
    parser.add_argument('--deploy-flask', action='store_true', help='Deploy sample Flask app')
    args = parser.parse_args()

    if args.hostname:
        logger.info(f"Setting hostname to {args.hostname}")
        set_hostname(args.hostname)

    if args.user:
        logger.info(f"Creating user: {args.user}")
        create_user(args.user)

    if args.install:
        logger.info(f"Installing packages: {args.install}")
        install_packages(args.install)

    if args.deploy_flask:
        logger.info("Deploying Flask app")
        deploy_flask_app()

if __name__ == '__main__':
    main()

# installer.py
import subprocess
import shutil

def install_packages(packages):
    for pkg in packages:
        if shutil.which(pkg) is None:
            subprocess.run(["sudo", "apt-get", "install", "-y", pkg], check=True)
        else:
            print(f"{pkg} is already installed.")

# user_manager.py
import subprocess
import pwd

def create_user(username):
    try:
        pwd.getpwnam(username)
        print(f"User '{username}' already exists.")
    except KeyError:
        subprocess.run(["sudo", "useradd", "-m", username], check=True)
        print(f"User '{username}' created.")

# config_editor.py
import subprocess

def set_hostname(hostname):
    with open("/etc/hostname", "w") as f:
        f.write(hostname + "\n")
    subprocess.run(["sudo", "hostnamectl", "set-hostname", hostname], check=True)

# deploy.py
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

# logger.py
import logging

def setup_logging():
    logger = logging.getLogger('autobox')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('autobox.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
