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
