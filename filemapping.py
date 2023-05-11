import os
from PIL import Image, ImageDraw, ImageFont

# Set the font to be used for the text
font = ImageFont.truetype("arial.ttf", 16)

# Set the size of each image
image_width = 800
image_height = 600

# Set the overlap between images
overlap = 50

# Set the base directory for the search
base_dir = input("Enter the base directory path: ")
output_folder = "output_folder"

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

    

# Initialize the x and y coordinates
x, y = 0, 0

# Initialize the image counter
image_num = 1

# Initialize the current image
current_image = Image.new('RGB', (image_width, image_height), color='white')

# Initialize the draw object for the current image
draw = ImageDraw.Draw(current_image)

# Walk through the directory tree and draw the images
for root, dirs, files in os.walk(base_dir):
    # Calculate the maximum width and height of the current directory
    max_width = 0
    total_height = 0
    for file in files:
        text_width, text_height = draw.textsize(file, font=font)
        max_width = max(max_width, text_width)
        total_height += text_height

    # Check if the current directory fits in the current image
    if y + total_height > image_height:
        # Save the current image and increment the image counter
        current_image.save(f"directory_tree_{image_num}.png")

        # Initialize a new image and draw object
        current_image = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(current_image)

        # Reset the x and y coordinates
        x, y = 0, 0

        # Increment the image counter
        image_num += 1

    # Draw the files in the current directory
    for file in files:
        text_width, text_height = draw.textsize(file, font=font)
        draw.text((x, y), file, fill='black', font=font)
        y += text_height

    # Add the directory name to the current image
    dir_name = os.path.basename(root)
    dir_width, dir_height = draw.textsize(dir_name, font=font)
    draw.text((x, y), f"-> {dir_name}", fill='black', font=font)
    y += dir_height

    # Draw the arrow pointing to the next level
    arrow_start_x = x + dir_width + overlap
    arrow_start_y = y - dir_height
    arrow_end_x = arrow_start_x + overlap
    arrow_end_y = arrow_start_y + dir_height
    draw.line((arrow_start_x, arrow_start_y, arrow_end_x, arrow_end_y), fill='black', width=1)

    # Update the x and y coordinates
    x = arrow_end_x + overlap
    y = arrow_end_y - dir_height

# Save the last image
current_image.save(f"directory_tree_{image_num}.png")

# Merge all the images into a single image
images = []
for filename in os.listdir():
    if filename.startswith('directory_tree_') and filename.endswith('.png'):
        images.append(Image.open(filename))

merged_image = Image.new('RGB', (image_width, image_height * len(images)), color='white')
y_offset = 0
for image in images:
    merged_image.paste(image, (0, y_offset))
    y
