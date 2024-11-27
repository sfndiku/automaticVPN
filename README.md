# Auto-Connect VPN at Startup

This project provides a script and systemd service to automatically connect to a ProtonVPN server at startup on a Linux system. The script randomly selects a VPN configuration file from a specified directory and connects to the VPN using OpenVPN with provided credentials.

## Prerequisites

- Python 3
- OpenVPN
- ProtonVPN account

## Setup

### Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/sfndiku/automaticVPN.git
```


### Step 2: Install Required Packages

Make sure Python and OpenVPN are installed

in Ubuntu and other debian based systems:
```bash
sudo apt install python3 python3-pip openvpn
```

in Arch Linux:
```bash
sudo pacman -S openvpn python
```
in CentOS/RHEL:
```bash
sudo yum install python3 python3-pip openvpn
```
in Fedora:
```bash
sudo dnf install python3 python3-pip openvpn
```


### Step 3: Set Up VPN Configuration Files
Place your ProtonVPN configuration files (.ovpn) in the configs directory within the cloned repository. In order to do this:

1. You need to have a ProtonVPN account
2. Sign in to your account
3. go to account page, click on Downloads, scroll down to OpenVPN configuration files
4. Choose the platform, protocol(most likely UDP), and click free server configs(assuming you do not have a paid subscription)
5. Download the necessary configuration files which suite you at least 5
6. Put those files in the config directory within you cloned repository for simplicity.


### Step 4: Edit the Python Script
Edit the connect_vpn.py script to set the path to your VPN configuration files:
```bash
VPN_CONFIG_DIR = '/path/to/config/files'  # Change this to the path where your .ovpn files are stored which is the config folder within the cloned repo
```

### Step 5: Set Environment Variables
To securely store your ProtonVPN credentials, set the environment variables in the systemd service file. How? I'll tell you how.

1. I have given the .service file in this repo, copy that and put it in the /etc/systemd/system/ folder.
2. Now in the .service file's line
   
   ```bash
   ExecStart=/usr/bin/env python3 /path/to/your/.py/file
   ```
   change the path of the .py file to your actual .py file which is in the cloned repo (connect_vpn.py)

3. Replace your_actual_username and your_actual_password in the .service file with your ProtonVPN credentials which you can get in the accounts page of protonvpn in OpenVPN / IKEv2 username section

### Step 6: Make the Python Script Executable

Make the connect_vpn.py script executable:
```bash
chmod +x /path/to/your/connect_vpn.py
```
which will be in your cloned repo.

### Step 7: Enable and Start the Systemd Service
Enable and start the systemd service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable connect_vpn.service
sudo systemctl start connect_vpn.service
```

### Step 8: Check if it is working properly
Go to [DNS leak test](https://dnsleaktest.com) site and check your DNS

### Step 9: Reboot your system
Reboot your system and check dnsleaktest.com


## Contact
Contact me via email <sfnbusiness01@gmail.com>.

> PS. feel free to modify and use it for your own requirements

