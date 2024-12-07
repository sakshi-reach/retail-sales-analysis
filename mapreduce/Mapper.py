#!/usr/bin/env python3
import sys

# Read each line from stdin
for line in sys.stdin:
    # Strip the line of leading/trailing whitespaces
    line = line.strip()
    
    # Split the line into fields based on tab separator
    fields = line.split('\t')
    if len(fields) == 3:  # Ensure we have three fields
        key = fields[0]  # First field is the key
        value = fields[2]  # Third field is the value
        
        # Emit key-value pairs (key, value)
        print(f"{key}\t{value}")

