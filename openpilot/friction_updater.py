#!/usr/bin/env python3
import time
import os
from common.params import Params
from cereal import messaging

# Ensure the directory exists
# os.makedirs('/data/params/d', exist_ok=True)

params = Params()

# Set up the messaging socket
sm = messaging.SubMaster(['carState'])

last_friction = None
last_write_time = 0
WRITE_INTERVAL = 1.0  # Write at most every 1 seconds

def update_friction():
    global last_friction, last_write_time
    sm.update()
    vEgo = sm['carState'].vEgo
    
    if vEgo > 17.8:           # > 45 mph
        friction = 0
    elif 9.0 <= vEgo <= 17.79: # 20-45 mph
        friction = 17
    elif vEgo < 8.99:          # < 20 mph
        friction = 25

    current_time = time.time()
    if friction != last_friction and current_time - last_write_time >= WRITE_INTERVAL:
        Params().put("TorqueFriction", str(friction).encode())
        last_friction = friction
        last_write_time = current_time
        print(f"Updated friction to {friction} (vEgo: {vEgo:.2f} m/s)")

while True:
    update_friction()
    time.sleep(0.5)  # Still update every 0.5 seconds, but write less frequently
