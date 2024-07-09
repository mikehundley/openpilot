#!/bin/bash

if pgrep -f "[m]tla.sh" > /dev/null || ps aux | grep "[m]tla.sh" > /dev/null; then
      echo "mtla.sh is running"
  else
      echo "mtla.sh is not running"
  fi

while true; do
  # Check to see if friction_updater.py and mtla.sh are running
  if pgrep -f /data/openpilot/openpilot/friction_updater.py > /dev/null; then
      echo "friction_updater.py is running"
  else
      echo "friction_updater.py is not running"
  fi
  
  echo "Current Friction = $(cat /data/params/d/TorqueFriction)"
  
  sleep 10
done
