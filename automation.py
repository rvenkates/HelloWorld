# automation.py
 
# run `netstat -i` in a loop once every .1 sec for 1 sec in total duration (10 times)
# each time I run, I want to capture the # of tx, rx bytes/packets for one iface
# collection these measurements into a dictionary
#   { timestamp: { 'rx': 123, 'tx': 533 }, timestamp+1: ... }
# -> output as JSON

import time
import datetime
import json
import subprocess

measurement = {}
stats = {}
for x in range(10):
    now = str(datetime.datetime.now())
    output = subprocess.check_output(['netstat', '-i', '-I', 'en0'])
    for line in output.splitlines():
        if line.startswith('en0'):
             name, _, _, _, rx, _, tx, _, _  = line.split()
             measurement[now] = {'Name': name, 'Receive': rx, 'Transmit': tx}
             break
    time.sleep(.1)

print json.dumps(measurement, indent=1)

