# map.py - Write bytes to file
import os

# The map data
# First digit: room layout
# Second digit: door layout
# map size: 256 bytes
# 32 columns is here           v
data = """
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000030000000000000000
00000000000002010200000000000000
00000000000000030000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
"""

# 10x12 room layouts
# room layout size: 128 bytes
# 10x12 = 120 bytes plus 8 at the end for padding
# 24 columns is here   v
data = data + """
000000000000000000000000
000101000000000000010100
000100000000000000000100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
000100000000000000000100
000101000000000000010100
000000000000000000000000
0000000000000000
"""

# Remove the newlines
data = data.translate(None, '\n')

# Convert from string to binary data
bin_data = data.decode("hex")

# Remove old file if it exists
if os.path.exists('mapdata'):
    os.remove('mapdata')

# Open the file in 'write binary' mode
out = open('mapdata', 'wb')

# Write to the file
i = 0
while i < len(bin_data):
    byte = bin_data[i]
    out.write(byte)
    i += 1

# Close the file
out.close()
