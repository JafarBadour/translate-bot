#!/bin/bash
sudo apt-get install git
sudo apt update
sudo apt install -y docker.io
sudo docker pull jafarbadour/telegram-translator-bot:latest
mkdir transbot
git clone https://github.com/JafarBadour/translate-bot.git transbot
sudo apt install -y python3-pip
cd transbot
pip3 install -r requirements.txt
