#!/bin/bash
echo "[!] Installing 1 GB 600 mb"
sleep 20
clear
echo "[!] Updating"
apt update -y
clear
echo "[!] Install"
apt install nmap curl perl python python2 php wget -y
apt install python3-pip -y
apt install python2-pip -y
pkg install whois -y
clear
echo "[!] Install pip"
pip3 install -r requirements.txt
pip2 install -r requirements.txt
pip3 install -r requirements-dev.txt
pip2 install -r requirements-dev.txt
pip2 install request
pip2 install requests
pip3 install request
pip2 install colorama
pip3 install colorama
chmod +x *
chmod +x name/username.sh
echo "[!] Upgrading"
apt upgrade -y
apt install spd -y
apt install festival -y
apt install festival speech-tools -y
apt install festvox-ru -y
apt install speech-dispatcher -y
pip3 install SpeechRecognition
apt install pkg-config -y
pkg install pkg-config -y
apt install libusb-1.0-0-dev libusb-1.0-0 libncurses5-dev libtecla1 -y
apt install python3-pyaudio -y
echo "[!] Install ADB"
chmod +x *
./InstallTools.sh
echo "[!] Install metasploit"
chmod +x *
./metasploit.sh
apt install ruby -y
pkg install ruby -y
pkg install unstable-repo -y
pkg install metasploit -y
apt update -y
./installsherman.sh
