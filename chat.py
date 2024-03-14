import os
import time

# Get a list of files in the current directory
files = os.listdir()

# Iterate over each file
for file in files:
    # Read and print the contents of the file
    with open(file, 'r') as f:
        print(f.read())
    
    # Introduce a 2-second delay before processing the next file
    time.sleep(2)
