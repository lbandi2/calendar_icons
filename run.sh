#!/bin/bash

mkdir -p logs
cd /home/sergio/scripts/calendar_icons/
find logs -type f -mtime +30 -delete
. ./env/bin/activate
/home/sergio/scripts/calendar_icons/env/bin/python3 /home/sergio/scripts/calendar_icons/main.py >> logs/calendar_icons-"`date +"%Y-%m-%d_%H.%M.%S"`".log 2>&1
deactivate
