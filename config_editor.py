import subprocess

def set_hostname(hostname):
    with open("/etc/hostname", "w") as f:
        f.write(hostname + "\n")
    subprocess.run(["sudo", "hostnamectl", "set-hostname", hostname], check=True)
