#!/bin/bash
sudo apt update
sudo apt install snapd -y
sudo apt install python3-pip -y
pip3 install flask
pip3 install flask_restful
sudo apt install python3-flask -y
pip3 install pymongo
sudo ufw allow 5000
sudo su
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=flask_server.py
flask run --host=0.0.0.0