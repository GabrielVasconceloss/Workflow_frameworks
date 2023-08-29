#!/bin/bash

sleep 10

cd /home/icetar/workflow/

gunicorn -w 4 -b 192.168.0.48:5000 app:app

