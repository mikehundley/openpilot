# Check to see if friction_updater.py is running
if pgrep -f /data/openpilot/openpilot/friction_updater.py > /dev/null; then
    echo "friction_updater.py is running"
else
    echo "friction_updater.py is not running"
fi
