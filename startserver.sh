#!/bin/bash 
sudo ./venv/bin/flask run --host=0.0.0.0 --port=80 >> log.txt 2>&1 &

