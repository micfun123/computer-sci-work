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
#make file output_file 
output_file = input("Enter the output file name: ")
try :
    os.mkdir(output_file)
except FileExistsError:
    print("File already exist")



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
        current_image.save(output_file + f"/directory_tree_{image_num}.png")
        image_num += 1

        # Initialize a new image and draw object
        current_image = Image.new('RGB', (image_width, image_height), color='white')
        draw = ImageDraw.Draw(current_image)

        # Reset the y coordinate
        y = 0

    # Add the directory name to the current image
    dir_name = os.path.basename(root)
    dir_width, dir_height = draw.textsize(dir_name, font=font)
    draw.text((x, y), f"└── {dir_name}", fill='black', font=font)
    y += dir_height

    # Draw the files in the current directory
    for file in files:
        text_width, text_height = draw.textsize(file, font=font)
        draw.text((x + overlap, y), f"├── {file}", fill='black', font=font)
        y += text_height

    # Add an arrow to the end of the directory name
    if dirs:
        arrow_width, arrow_height = draw.textsize("└──", font=font)
        draw.text((x + arrow_width, y - dir_height), "└──►", fill='black', font=font)

    # Update the y coordinate
    y += overlap

# Save the last image to the output folder
current_image.save(output_file + f"/directory_tree_{image_num}.png")

