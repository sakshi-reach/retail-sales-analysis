#!/usr/bin/env python3
import sys

current_key = None
current_value = 0

# Read each line from stdin
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    
    # Try to convert the value to an integer
    try:
        value = int(value)
    except ValueError:
        continue
    
    # If the key is the same as the previous one, accumulate the value
    if key == current_key:
        current_value += value
    else:
        # If the key changes, print the result for the previous key
        if current_key:
            print(f"{current_key}\t{current_value}")
        
        # Set the new key and reset the value
        current_key = key
        current_value = value

# Output the last key-value pair if exists
if current_key:
    print(f"{current_key}\t{current_value}")

