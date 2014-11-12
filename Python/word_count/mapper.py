#!/usr/bin/env python

import sys

for line in sys.stdin:
        line = line.strip()
        keys = line.split()
        for key in keys:
                value = 1
                key = key.lower()
                remove = "!@?/\\`~<>#$%^&*(),.;:[]\"{}=+'-_"
                print filter(lambda x: not (x in remove), key) + "\t%d" % (value)
