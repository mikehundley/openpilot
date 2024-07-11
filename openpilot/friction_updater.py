#!/usr/bin/env python3
import time
import logging
from logging.handlers import RotatingFileHandler
from common.params import Params
from cereal import messaging

# Set up logging with rotation
log_handler = RotatingFileHandler(
    'friction_updater.log',
    maxBytes=10*1024*1024,  # 10 MB
    backupCount=5  # Keep up to 5 backup log files
)
log_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

class FrictionUpdater:
    def __init__(self):
        self.params = Params()
        self.sm = messaging.SubMaster(['carState'])
        self.last_friction = self.get_current_friction()
        self.last_write_time = 0
        self.WRITE_INTERVAL = 3  # Write at most every 3 seconds

    def get_current_friction(self):
        try:
            current_friction = self.params.get("TorqueFriction")
            if current_friction is not None:
                return int(current_friction)
            return None
        except Exception as e:
            logging.error(f"Error reading current TorqueFriction: {e}")
            return None
    
    LOW_SPEED_THRESHOLD = 9.0	  # ~20 mph
    HIGH_SPEED_THRESHOLD = 20.12  # ~45 mph
    
    HIGH_FRICTION = 25
    MEDIUM_FRICTION = 18
    LOW_FRICTION = 0
    
    def update_friction(self):
        self.sm.update()
        vEgo = self.sm['carState'].vEgo

        if vEgo < LOW_SPEED_THRESHOLD:           
            return HIGH_FRICTION
        elif LOW_SPEED_THRESHOLD <= vEgo < HIGH_SPEED_THRESHOLD: 
            return MEDIUM_FRICTION
        else:          
            return LOW_FRICTION

        current_time = time.time()

        if friction != self.last_friction and current_time - self.last_write_time >= self.WRITE_INTERVAL:
            logging.info(f"Updating TorqueFriction from {self.last_friction} to {friction}")
            try:
                self.params.put("TorqueFriction", str(friction).encode())
                self.last_friction = friction
                self.last_write_time = current_time
                logging.info(f"Updated friction to {friction} (vEgo: {vEgo:.2f} m/s)")
            except Exception as e:
                logging.error(f"Error writing TorqueFriction: {e}")

    def run(self):
        while True:
            try:
                self.update_friction()
                time.sleep(1.0)  # Still update every 1 seconds, but write less frequently
            except Exception as e:
                logging.error(f"Error occurred: {e}")
                time.sleep(5)  # Wait for 5 seconds if an error occurs before retrying

if __name__ == "__main__":
    updater = FrictionUpdater()
    updater.run()
