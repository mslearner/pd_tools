#!/usr/bin/env python3
import paramiko
import io
import pexpect
import argparse
import argparse
import os
import subprocess
import sys
import locale
import time
import jwt
from subprocess import Popen, PIPE, CalledProcessError
import pexpect


def create_jwt(private_key, expiration=60):
    now = int(time.time())
    payload = {
        "aud": "pdewan-qemu",
        "sub": "pdewan",
        "ops": [
            "shl"
        ],
        "exp": now+expiration
    }
    encrypted = jwt.encode(
        payload,
        key=private_key,
        algorithm="ES384"
    )

    encrypted = encrypted.decode('utf-8')

    return encrypted


def ssh_copy_id(device_hostname, l_username, token="", ignore_result: bool = False, stdout: bool = True):

    template_ssh_args = ["ssh"]
    template_ssh_args += [f"{l_username}@{device_hostname}"]
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(device_hostname, username=l_username, password=token)
    stdin, stdout, stderr = client.exec_command('hostname')
    for line in io.TextIOWrapper(stdout, encoding="utf-8"):
        print("Logged into the device, hostname="+line)

    key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    print("Copied the public key to the device --- enjoy!!!!")


# def provision(device_hostname):
#     print("call server to provision")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("device_hostname",
                        help="Device hostname or IP address")
    args = parser.parse_args()
    print("provisioning the device!")
    # provision(args.device_hostname)
    login(args.device_hostname)

    print("**Finished**")


def login(device_hostname):
    with open('jwt_ec_private.pem', 'r') as file:
        private_key = file.read()
    jwt = create_jwt(private_key)
    print("Received the token!")
    print("jwt="+jwt)
    device_id = ssh_copy_id(
        device_hostname, l_username="restricted-admin", token=jwt)


if __name__ == "__main__":
    main()
