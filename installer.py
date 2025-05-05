import subprocess
import shutil

def install_packages(packages):
    for pkg in packages:
        if shutil.which(pkg) is None:
            subprocess.run(["sudo", "apt-get", "install", "-y", pkg], check=True)
        else:
            print(f"{pkg} is already installed.")
