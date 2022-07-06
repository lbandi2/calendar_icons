#!/bin/bash

mkdir -p logs
cd /home/sergio/scripts/calendar_geocode/
. ./env/bin/activate
/home/sergio/scripts/calendar_geocode/env/bin/python3 /home/sergio/scripts/calendar_geocode/main.py >> logs/calendar_geocode-"`date +"%Y-%m-%d_%H.%M.%S"`".log 2>&1
deactivate
