import os

bitmap_path = os.path.join(os.path.dirname(__file__), 'bitmap.bmp')

with open(bitmap_path, 'rb') as f:
    file_data = bytearray(f.read())

# Find the most common color
colours = {}

for i in range(54, len(file_data), 3):
    b = file_data[i]
    g = file_data[i + 1]
    r = file_data[i + 2]

    colour = (r, g, b)

    if colour in colours:
        colours[colour] += 1
    else:
        colours[colour] = 1

most_common_colour = max(colours, key=colours.get)

print("Most common color:", most_common_colour)

# Change the most common color to pink (255, 192, 203)
for i in range(54, len(file_data), 3):
    b = file_data[i]
    g = file_data[i + 1]
    r = file_data[i + 2]

    colour = (r, g, b)

    if colour == most_common_colour:
        file_data[i:i+3] = bytearray([203, 192, 255])  # Assigning new values using bytearray

with open('pink.bmp', 'wb') as f:
    f.write(file_data)
