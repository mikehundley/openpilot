#!/bin/bash

while true
do
    # Create MapTargetLatA parameter
    echo -en "2.5" > /data/params/d/MapTargetLatA
    echo -en "2.5" > /dev/shm/params/d/MapTargetLatA
    
    # Wait for 60 seconds before the next iteration
    sleep 60
done
