#!/bin/bash

VALUE="2.8"
PARAMS="/data/params/d/MapTargetLatA"
MEM_PARAMS="/dev/shm/params/d/MapTargetLatA"

write_value() {
    echo -n "$VALUE" > "$PARAMS"
    sudo echo -n "$VALUE" > "$MEM_PARAMS"
   # echo "Value updated to $VALUE"
}

while true
do
    if [ ! -f "$PARAMS" ] || [ ! -f "$MEM_PARAMS" ]; then
        # File doesn't exist, write the value
        write_value
    else
        # Check if the current content is different from VALUE
        CURRENT_VALUE=$(cat "$PARAMS")
        if [ "$CURRENT_VALUE" != "$VALUE" ]; then
            write_value
        else
            :
        fi
    fi
    
    # Wait for 60 seconds before the next iteration
    sleep 60
done
