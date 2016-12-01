#!/bin/bash

function log {
while [ 1 ]   # Endless loop.
do
  echo "Log stuff"
  sleep 30
done
}

log &

# Wait to start server.
sleep ${START_WAIT_TIME:-0}

/usr/sbin/nginx
