"""
Module to decrypt/encrypt the config file.
How to Run: python crypt.py encrypt -c /path/to/config.ini -k key_to_encrypt/decrypt
"""

import argparse
import sys
import base64
import uuid
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


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
        length=32,
        salt=salt,
        iterations=390000,
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
            "Please make sure current user have permission to edit the config "
            "file.")
        sys.exit()


def encrypt(fernet, configfile):
    """
    Encrypt the file content.
    """
    config = read_file_content(configfile)
    # if "export_cluster_config" not in str(config):
    #     print("File is already encrypted, skipping!!")
    #     sys.exit()
    encrypted_config = fernet.encrypt(config)
    write_file_content(configfile, encrypted_config)
    print(f"Successfully encrypted the config file '{configfile}'")


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
        write_file_content(configfile, decrypted_config)
    except InvalidToken:
        print("Please provide valid key to 'decrypt' the file contents.")
        sys.exit()
    print(f"Successfully decrypted the config file {configfile}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", action="store", help="Action to be performed, encrypt/decrypt"
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
    args = parser.parse_args()
    config_file = args.config or "config.ini"
    if not args.key:
        print(f"Please provide a valid 'key' to '{args.action}'")
        sys.exit()

    key = generate_key(args.key)
    fernet_key = Fernet(key)
    if args.action.lower() == "encrypt":
        encrypt(fernet_key, config_file)
    elif args.action.lower() == "decrypt":
        decrypt(fernet_key, config_file)
    else:
        print("Invalid action provided, exiting!")
        sys.exit()
