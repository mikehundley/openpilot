#!/usr/bin/env python3
import capnp
import os
import time
from common.params import Params

# Load the car.capnp schema
car_capnp = capnp.load(os.path.expanduser('~/openpilot/cereal/car.capnp'))

params = Params()

def update_friction():
    # Read the current vEgo value
    car_state = messaging.recv_one(socket)
    vEgo = car_state.carState.vEgo

    # Determine the appropriate friction value
    if vEgo > 22.4:  # 50 mph in m/s
        friction = 0
    else:
        friction = 17

    # Update the TorqueFriction parameter
    params.put("TorqueFriction", str(friction).encode())

# Main loop
while True:
    update_friction()
    time.sleep(0.5)  # Update every 100ms, adjust as needed
