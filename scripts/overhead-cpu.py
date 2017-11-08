#!/usr/bin/env python3
import subprocess
import time

timeout = time.time() + 60*15

def cpu():
    subprocess.call(['python3','-c','for i in range(int(1e8)): t=12341234234.234 / 2.0'])
    return;

while True:
    cpu()
    if time.time() > timeout:
        subprocess.exit(0)
        break

