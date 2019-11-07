#!/bin/bash
sudo apt update -y
sudo apt install snapd -y
sudo apt install python3-pip -y
pip3 install flask
pip3 install flask_restful
sudo apt install python3-flask -y
export FLASK_APP=flask_server.py
flask run