#!/bin/bash

VALUE="2.8"

while true
do
    # Create MapTargetLatA parameter
    echo -en "$VALUE" > /data/params/d/MapTargetLatA
    sudo echo -en "$VALUE" > /dev/shm/params/d/MapTargetLatA
    
    # Wait for 60 seconds before the next iteration
    sleep 60
done
