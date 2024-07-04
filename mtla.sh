#!/bin/bash

while true
do
    # Make directory if it doesnt exist
    sudo mkdir -p /dev/shm/params/d
    sudo mkdir -p /data/params/d
    
    # Create MapTargetLatA parameter
    echo -en "2.8" > /data/params/d/MapTargetLatA
    echo -en "2.8" > /dev/shm/params/d/MapTargetLatA
    
    # Wait for 60 seconds before the next iteration
    sleep 60
done
