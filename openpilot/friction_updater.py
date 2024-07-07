#!/usr/bin/env python3

import time
from common.params import Params
from cereal import messaging

params = Params()

# Set up the messaging socket
sm = messaging.SubMaster(['carState'])

def update_friction():
    # Update carState
    sm.update()

    # Read the current vEgo value
    vEgo = sm['carState'].vEgo

    # Determine the appropriate friction value
    if vEgo > 22.4:  # 50 mph in m/s
        friction = 0
    else:
        friction = 17

    # Update the TorqueFriction parameter
    params.put("TorqueFriction", str(friction).encode())

    # Update the TorqueFriction parameter
    params.put("TorqueFriction", str(friction).encode())
    print(f"Updated friction to {friction} (vEgo: {vEgo:.2f} m/s)")

# Main loop
while True:
    update_friction()
    time.sleep(2.0)  # Update every 2 seconds, adjust as needed
