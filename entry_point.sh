#!/bin/bash
touch /app/logs/gunicorn.log
touch /app/logs/gunicorn-access.log
#tail -n 0 -f /app/logs/gunicorn*.log &
gunicorn --workers 3 \
         -b 0.0.0.0:8080 \
         --reload app.main:application \
         --log-level=info  \
         --log-file=/app/logs/gunicorn.log \
         --access-logfile=/app/logs/gunicorn-access.log
