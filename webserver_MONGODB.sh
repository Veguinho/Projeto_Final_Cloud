#!/bin/bash
cd /
sudo apt update
sudo apt install snapd -y
sudo apt install python3-pip -y
pip3 install flask
pip3 install flask_restful
sudo apt install python3-flask -y
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
sudo echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo mkdir -p /data/db
sudo chmod 744 /data/db
sudo su
cp /Projeto_Final_Cloud/reboot_mongo.service /etc/systemd/system
chmod 664 /etc/systemd/system/reboot_mongo.service
systemctl daemon-reload
systemctl start reboot_mongo.service
systemctl enable reboot_mongo.service