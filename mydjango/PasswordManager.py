import getpass
import hashlib
from base64 import urlsafe_b64encode
import os
from cryptography.fernet import Fernet
import yaml
from typing import Dict, Optional


class PasswordManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.key = self.get_key()

        if not os.path.exists(self.file_path):
            self.initialize_file()

    def get_key(self) -> bytes:

        if os.path.exists(".key"):
            with open(".key", "rb") as file:
                key = file.read()
            try:
                Fernet(key)
                return key
            except ValueError:
                raise ValueError("Die vorhandene .key-Datei enthält keinen gültigen Fernet-Schlüssel.")
        else:
            key = getpass.getpass("Enter the key: ")
            hashed_key = hashlib.sha256(key.encode()).digest()
            fernet_key = urlsafe_b64encode(hashed_key[:32])
            with open(".key", "wb") as file:
                file.write(fernet_key)
        return fernet_key

    def initialize_file(self) -> None:
        password = getpass.getpass("Enter the Authentication password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            encrypted_data = Fernet(self.key).encrypt(b"{}")
        except ValueError:
            raise ValueError("Error encrypting the file. The key is invalid.")

        with open(self.file_path, "w") as file:
            data = {"auth_data": hashed_password, "passwords": encrypted_data}
            yaml.dump(data, file, default_flow_style=False)

    def authenticate(self) -> bool:
        password = getpass.getpass("Enter the Authentication password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open(self.file_path, "r") as file:
            data = yaml.safe_load(file)
            return hashed_password == data["auth_data"]

    def load_passwords(self) -> Dict[str, str]:
        with open(self.file_path, "r") as file:
            data = yaml.safe_load(file)
            ecrypted_data = data["passwords"]

        decrypted_data = Fernet(self.key).decrypt(ecrypted_data)
        return yaml.safe_load(decrypted_data)

    def save_passwords(self, passwords: Dict[str, str]) -> None:
        ecrypted_data = Fernet(self.key).encrypt(yaml.dump(passwords).encode())

        with open(self.file_path, "r") as file:
            data = yaml.safe_load(file)

        data["passwords"] = ecrypted_data

        with open(self.file_path, "w") as file:
            yaml.dump(data, file, default_flow_style=False)

    def add_password(self, identifier: str, password: str) -> None:
        if not self.authenticate():
            print("Authentication failed.")
            return

        passwords = self.load_passwords()
        passwords[identifier] = password

        self.save_passwords(passwords)
        print(f"Password for {identifier} saved successfully.")

    def get_password(self, identifier: str) -> Optional[str]:
        if not self.authenticate():
            print("Authentication failed.")
            return

        passwords = self.load_passwords()
        if identifier in passwords:
            return passwords[identifier]
        print(f"Password for {identifier} not found.")
        return None


manager = PasswordManager("passwords.yaml")
# manager.add_password("example1", "test")
# manager.add_password("example2", "test2")
# manager.get_password("nonexist")
password = manager.get_password("example1")
print(f"Passwords für example1: {password}")
