#!/bin/bash
sudo apt update
sudo apt install snapd
sudo apt install python3-pip
pip3 install flask
pip3 install flask_restful
sudo apt install python3-flask
export FLASK_APP=flask_server.py
flask run