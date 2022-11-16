"""
Module to decrypt/encrypt the config file.
How to Run:
    python secure_config_file.py --operation encrypt -c /path/to/config.ini \
        -k key_to_encrypt/decrypt
"""

import argparse
import base64
import datetime
import sys
import uuid

from distutils.util import strtobool
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

ITERATIONS = 390000
LENGTH = 32


def generate_key(password):
    """
    Generate key which will be used for encryting and decrypting the file
    content.
    return key
    """
    # convert to bytes.
    password = bytes(password, "utf-8")
    salt = (uuid.getnode()).to_bytes(8, byteorder="big")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=LENGTH,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend(),
    )
    pass_key = base64.urlsafe_b64encode(kdf.derive(password))
    return pass_key


def read_file_content(file_name):
    """
    Read the file content as bytes.
    """
    try:
        with open(file_name, "rb") as file_obj:
            return file_obj.read()
    except FileNotFoundError:
        print(f"Failed to find the config file '{file_name}'.")
        sys.exit()


def write_file_content(file_name, content):
    """
    Write the data content to the file as bytes.
    """
    try:
        with open(file_name, "wb") as file_obj:
            file_obj.write(content)
            return content
    except FileNotFoundError:
        print(f"Failed to find the config file '{file_name}'.")
        sys.exit()
    except PermissionError:
        print(
            "Please make sure current user have permission to edit the config " "file."
        )
        sys.exit()


def encrypt(fernet, configfile):
    """
    Encrypt the file content.
    """
    config = read_file_content(configfile)
    encrypted_config = fernet.encrypt(config)
    write_file_content(WRITE_FILE_NAME, encrypted_config)
    print(f"Successfully encrypted the config file '{configfile}' to '{WRITE_FILE_NAME}'")


def decrypt(fernet, configfile):
    """
    Decrypt the file content.
    """
    try:
        config = read_file_content(configfile)
        if "export_cluster_config" in str(config):
            print("File is already decrypted, skipping!!")
            sys.exit()
        decrypted_config = fernet.decrypt(config)
        write_file_content(WRITE_FILE_NAME, decrypted_config)
    except InvalidToken:
        print("Please provide valid key to 'decrypt' the file contents.")
        sys.exit()
    print(f"Successfully decrypted the config file '{configfile}' to '{WRITE_FILE_NAME}'")


if __name__ == "__main__":
    # global WRITE_FILE_NAME
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--operation",
        "-o",
        action="store",
        required=True,
        help="Operation to be performed, encrypt/decrypt"
    )
    parser.add_argument(
        "--config",
        "-c",
        action="store",
        help="Path of the configuration file to encrypt/decrypt",
    )
    parser.add_argument(
        "--key",
        "-k",
        action="store",
        help="Key to encrypt/decryt the configuration file",
    )
    parser.add_argument(
        "--overwrite",
        action="store",
        default=True,
        type=strtobool,
        help="Flag to overwrite the configuration file"
    )
    args = parser.parse_args()
    config_file = args.config or "config.ini"
    if not args.key:
        print(f"Please provide a valid 'key' to '{args.operation}'")
        sys.exit()

    key = generate_key(args.key)
    WRITE_FILE_NAME = config_file
    if not args.overwrite:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        f_name, ext = config_file.split(".")
        WRITE_FILE_NAME = f_name + "_" + args.operation + "_" + timestamp + "." + ext

    fernet_key = Fernet(key)
    if args.operation.lower() == "encrypt":
        encrypt(fernet_key, config_file)
    elif args.operation.lower() == "decrypt":
        decrypt(fernet_key, config_file)
    else:
        print("Invalid action provided, exiting!")
        sys.exit()
