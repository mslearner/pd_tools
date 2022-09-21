#!/usr/bin/env python3
import argparse
import argparse
import os
import subprocess
import sys
import locale
import time
import jwt

def create_jwt(private_key, expiration=60):
        """
        Creates a signed JWT, valid for 60 seconds by default.
        The expiration can be extended beyond this, to a maximum of 600 seconds.

        :param expiration: int
        :return:
        """
        now = int(time.time())
        payload = {
            "aud": "pdewan-qemu",
            "sub": "pdewan",
            "ops": [
                 "shl"
             ]
        }
        encrypted = jwt.encode(
            payload,
            key=private_key,
            algorithm="ES384"
        )

        
        encrypted = encrypted.decode('utf-8')

        return encrypted

def run_ssh_command(cmd_args, device_hostname, username, token="", ignore_result: bool = False, stdout: bool = True):
    template_ssh_args = ["ssh"]
    template_ssh_args += [f"{username}@{device_hostname}"]
    result = subprocess.run(template_ssh_args + cmd_args, capture_output = True, encoding = locale.getpreferredencoding(False))

    if not ignore_result:
        if result.returncode != 0:
            printable_args = " ".join(cmd_args)
            sys.stderr.write(f"error: failed to run: {printable_args}\n")
            sys.stdout.write(result.stdout)
            sys.stderr.write(result.stderr)
            sys.exit(result.returncode)
        if stdout:
            return result.stdout

#https://stackoverflow.com/questions/19880190/interactive-input-output-using-python
def provision(device_hostname):
    device_id= run_ssh_command(["echo","sswws"], device_hostname,"provisioning")
    print("device_id="+device_id)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("device_hostname", help="Device hostname or IP address")
    parser.add_argument("-c", "--disable-strict-host-key-checking",
                    dest="disable_strict_host_key_checking",
                    help="Disable strict host key checking in ssh",
                    default=False,
                    action="store_true")

    args = parser.parse_args()
    print("provision first!")
    # provision(args.device_hostname)
    login(args.device_hostname)
    print("getting token for the id!")
    print("logging in!")

def login(device_hostname):
    with open('jwt_ec_private.pem', 'r') as file:
        private_key = file.read()
    jwt=create_jwt(private_key)
    print("jwt="+jwt)
    device_id= run_ssh_command(["echo","sswws"], device_hostname,username="restricted-admin",token=jwt)


if __name__ == "__main__":
    main()

