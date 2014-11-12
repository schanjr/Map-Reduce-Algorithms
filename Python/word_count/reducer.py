#!/usr/bin/env python

import sys

last_key = None
running_total = 0
lookup = {}

for input_line in sys.stdin:
#       input_line = input_line.strip()
        (this_key, value) = input_line.split("\t", 1)
        value = int(value)

        if last_key == this_key:  # if keys are matching, increase the running_total value
                running_total += value
        else: #if last_key is not matching, simply print it out. running_total is reset and last_key is matched with the current key
                if last_key:
                        print( "%s\t%d" % (last_key, running_total) )
                        lookup[running_total] = last_key
                running_total = value
                last_key = this_key
if last_key == this_key: #Extra if statement if last_key is matching again, print it out.
        print ( "%s\t%d" % (last_key, running_total) )
        lookup[running_total] = last_key

for look in sorted(lookup.keys(), reverse=True):
        print look, lookup[look]
