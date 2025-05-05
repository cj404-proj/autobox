import subprocess
import pwd

def create_user(username):
    try:
        pwd.getpwnam(username)
        print(f"User '{username}' already exists.")
    except KeyError:
        subprocess.run(["sudo", "useradd", "-m", username], check=True)
        print(f"User '{username}' created.")
