#!/usr/bin/env python3

import os
import random
import subprocess
import stat

VPN_CONFIG_DIR = '/path/to/config/files'  # Change this to the path where your .ovpn files are stored
USERNAME = os.getenv('PROTONVPN_USERNAME', 'fallback_username')  # Fallback for  testing and the actual username is stored in /etc/systemd/system/connect_vpn.service
PASSWORD = os.getenv('PROTONVPN_PASSWORD', 'fallback_password')  # Fallback for testing and the actual password is stored in /etc/systemd/system/connect_vpn.service

def connect_to_vpn():
    vpn_files = [f for f in os.listdir(VPN_CONFIG_DIR) if f.endswith('.ovpn')] # code line accessing .ovpn files
    if not vpn_files:
        print("No VPN configuration files found.")
        return
    
    selected_vpn = random.choice(vpn_files) # choosing a random .ovpn file
    vpn_path = os.path.join(VPN_CONFIG_DIR, selected_vpn)
    
    # Temporary storage of username and password, so that we can use it directly on the command line
    credentials_path = '/tmp/vpn_credentials.txt'
    with open(credentials_path, 'w') as cred_file:
        cred_file.write(f'{USERNAME}\n{PASSWORD}\n')
    
    # making the credential txt file readable by the stat module usinf the stat.S_IRUSR function
    os.chmod(credentials_path, stat.S_IRUSR) 

    try:
        subprocess.run(['sudo', 'openvpn', '--config', vpn_path, '--auth-user-pass', credentials_path]) # credentials_path is the file containning the temp username and pw
    finally:
        os.remove(credentials_path) # removing temp storage of username and pw

if __name__ == "__main__":
    if USERNAME == 'fallback_username' or PASSWORD == 'fallback_password':
        print("Please set the PROTONVPN_USERNAME and PROTONVPN_PASSWORD environment variables.") # for testing you could use these if it does not work properly
    else:
        connect_to_vpn()
