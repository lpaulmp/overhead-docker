#!/usr/bin/env python3
# Other command to overhead io  stress --vm-bytes $(awk '/MemFree/{printf "%d\n", $2 * 0.097;}' < /proc/meminfo)k --vm-keep -m 10

import subprocess
import time

timeout = time.time() + 60*15

def dd():
    subprocess.call(['dd','if=/dev/urandom','of=/tmp/space','bs=1GB','count=10'])
    return;

while True:
    dd()
    if time.time() > timeout:
        subprocess.exit(0)
        break

