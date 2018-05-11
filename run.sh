#!/bin/bash

trap "echo 'Received SIGINT'; exit" INT
trap "echo 'Received SIGTERM'; exit" TERM
trap "echo 'Received SIGERR'; exit" ERR
trap "kill 0" EXIT
echo "pid is $$"

function log {
while [ 1 ]   # Endless loop.
do
  echo "Log stuff"
  sleep 5
done
}

log &

/usr/sbin/nginx &
PID="$!"

wait $PID
