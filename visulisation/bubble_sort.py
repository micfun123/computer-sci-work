from PIL import Image, ImageDraw,ImageFont
import random


# Parameters for the animation
num_elements = 50
bar_width = 20
frame_duration = 50  # in milliseconds

# Generate random initial array
arr = [random.randint(1, 100) for _ in range(num_elements)]
max_value = max(arr)

# Function to visualize the array as an image
def visualize_array(arr, step):
    width = num_elements * bar_width
    height = max_value + 250  # Add extra space for labels and step information
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        x1 = x0 + bar_width
        y0 = height - val
        y1 = height
        draw.rectangle([x0, y0, x1, y1], outline=(0, 0, 0), width=2)

    # Add step information at the bottom, scaled proportionally
    step_text = f"Step {step + 1}"
    step_font_size = max(12, int((width / 20)))  # Adjust the 10 based on your preferences
    step_font = ImageFont.truetype("arial.ttf", step_font_size)  # You can specify a different font
    text_width, text_height = draw.textsize(step_text, font=step_font)
    text_x = (width - text_width) // 2
    text_y = height - text_height - 150
    draw.text((text_x, text_y), step_text, fill=(0, 0, 0), font=step_font)

    return image


# Bubble Sort Algorithm
def bubble_sort(arr):
    frames = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                frames.append(visualize_array(arr, len(frames)))
    
    return frames

# Create a GIF of the Bubble Sort process
frames = bubble_sort(arr)

# Save the frames as a GIF
frames[0].save("bubble_sort_animation.gif", save_all=True, append_images=frames[1:], duration=frame_duration, loop=0)
print("Done!")
