# map.py - Write map layout and room layout bytes to file
import os

# The map data
# First digit: room layout
# Second digit: door layout
# map size: 256 bytes
# segment 0 from start of file
# 32 columns is here           v
data = """
090A00090A000902020A0009020A000E
08050A08060003090A08020B0E03090B
000F030D050A0303030009020603080A
0003080A0003030705020B0F03030D06
0D010A0802010B080A000F080B03090B
000303000008020A080A0802020B0300
090B07020A0000030007020202020B00
03090B090504020102060009020A0000
03030906000E00030007020B00080000
030706080A0009050A0300090C00080A
080B070C03000300030300080A090A03
00090B0F080C030003080A0003030303
0901040B0000080A03000300080B0806
0307050A00090C030300080404040206
030E0008040B090B0E0F000E03080C03
080C000D0B000802020B00000802020B
"""

# 10x12 room layouts
# room layout size: 128 bytes
# 10x12 = 120 bytes plus 8 bytes at the end for 4 colors for walls and 4 colors for tiles
# formula for letter/character:
# 
# x: index in alphabet of letter 0 - 25
# y: segment of memory
# z: offset in segment
# 
# y = floor(x / 16)
# z = x mod 16
# 
# for encoding in map.py as hexadecimal digits
# first digit = y + 1 
# because first digit 0 indicates an empty tile
# second digit = z
def encodeStringAsSprites(text):
    encoded = ""
    text = text.lower()
    for c in text:
        x = (ord(c) - ord('a'))
        y = x // 16
        z = x % 16
        encoded = encoded + format(y + 1, '1x') + format(z, '1x')
    return encoded

print(encodeStringAsSprites("caves"))
print(encodeStringAsSprites("of"))
print(encodeStringAsSprites("mars"))
# tile is empty if tile type is 0
# segment 1
# 24 columns is here   v
data = data + """
000000000000000000000000
001210251422000000000000
001e15000000000000000000
001c10212200000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
008000000000000000006000
000000000000000000000000
000000000000000000000000
8060C000FF000000
"""
#^ colors are 128, 96, 128 for walls and 255, 00, 00 for tiles

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 2

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 3

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 4

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 5

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 6

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 7

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 8

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

data = data + """
000000000000000000000000
001011000000000000121300
002000000000000000002100
000000000000000000000000
000000000000000000000000
000000000000000000000000
000000000000000000000000
001000000000000000001000
001010000000000000101000
000000000000000000000000
0000000000000000
"""

# segment 9

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
