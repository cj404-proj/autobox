# README.md

# AutoBox: Infrastructure Bootstrapper

AutoBox is a Python-based command-line tool designed to simplify infrastructure tasks. It helps automate package installation, user creation, hostname configuration, and deploying a sample Flask application as a systemd service.

## 🚀 Features

- Install essential packages
- Create Linux users
- Change system hostname
- Deploy a simple Flask app
- Logging of all operations

## 📁 Project Structure

```
.
├── autobox.py              # Main entry script
├── installer.py            # Package installation logic
├── user_manager.py         # User creation
├── config_editor.py        # Hostname setter
├── deploy.py               # Flask deployment script
├── logger.py               # Logger configuration
└── autobox.log             # Log file (created at runtime)
```

## 🔧 Requirements
- Python 3.6+
- Linux environment (tested on Ubuntu)
- Sudo privileges

## ⚙️ How to Use

Run the script with various options:

```bash
python autobox.py --hostname myhost --user jayanth --install git curl --deploy-flask
```

### Options

| Argument        | Description                                  |
|----------------|----------------------------------------------|
| `--hostname`    | Sets the system hostname                     |
| `--user`        | Creates a new Linux user                     |
| `--install`     | Installs one or more packages via apt        |
| `--deploy-flask`| Deploys a sample Flask app                   |

## 🧪 Example Commands

### Set Hostname
```bash
python autobox.py --hostname devbox
```

### Create a User
```bash
python autobox.py --user devops
```

### Install Packages
```bash
python autobox.py --install git htop curl
```

### Deploy Sample Flask App
```bash
python autobox.py --deploy-flask
```

Visit `http://<your-server-ip>:5000` to view the Flask app once deployed.

## 📒 Logs
All logs are stored in `autobox.log`.

## 📚 Learning Outcomes
- Python `subprocess`, `argparse`, `logging`, and OS modules
- Linux user & package management
- Writing Python scripts for DevOps tasks
- Automating deployments using `systemd`

---

Happy Automating! ✨
