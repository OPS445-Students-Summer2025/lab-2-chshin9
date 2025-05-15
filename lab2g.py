#!/usr/bin/env python3

#Author: Charles Shin
#Author ID: 166315226
#Date Created: 2025/05/8

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(str(timer))
    timer = timer - 1

print("blast off!")
