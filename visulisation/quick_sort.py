from PIL import Image, ImageDraw, ImageFont
import random

# Parameters for the animation
num_elements = 150
bar_width = 20
frame_duration = 50

# Generate a random initial array
arr = [random.randint(1, 100) for _ in range(num_elements)]
max_value = max(arr)


# Function to calculate gradient color
def gradient_color(current, total):
    r = int(255 * (1 - current / total))
    g = int(255 * (1 - current / total))
    b = int(255 * (current / total))
    return (r, g, b)


# Function to visualize the array as an image
def visualize_array(arr, pivot_index=None, low_index=None, high_index=None, step=None):
    width = num_elements * bar_width
    height = max_value + 250
    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        x1 = x0 + bar_width
        y0 = height - val
        y1 = height
        color = gradient_color(i, len(arr))
        if i == pivot_index:
            color = (255, 0, 0)
        elif low_index <= i <= high_index:
            color = (0, 255, 0)
        draw.rectangle([x0, y0, x1, y1], outline=(255, 255, 255), width=2, fill=color)

    if step is not None:
        step_text = f"Step {step + 1}"
        step_font_size = max(12, int(width / 20))
        step_font = ImageFont.truetype("arial.ttf", step_font_size)
        text_width, text_height = draw.textsize(step_text, font=step_font)
        text_x = (width - text_width) // 2
        text_y = height - text_height - 150
        outline_color = (255, 255, 255)  # Outline color (black)
        fill_color = (255, 255, 255)  # Text color (white)
        draw.text(
            (text_x, text_y),
            step_text,
            fill=fill_color,
            font=step_font,
            stroke_width=2,
            stroke_fill=outline_color,
        )

    return image


# Quick Sort Algorithm
def quick_sort(arr, low, high, frames, step):
    if low < high:
        pivot_index, new_low, new_high, step = partition(arr, low, high, frames, step)
        step = quick_sort(arr, low, pivot_index - 1, frames, step)  # Update step here
        step = quick_sort(arr, pivot_index + 1, high, frames, step)  # Update step here
    return step


def partition(arr, low, high, frames, step):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            frames.append(visualize_array(arr, j, low, high, step))
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    frames.append(visualize_array(arr, i + 1, low, high, step))
    return i + 1, low, high, step + 1  # Increment step here


# Create a GIF of the Quick Sort process
frames = []
quick_sort(arr, 0, len(arr) - 1, frames, step=0)

# Save the frames as a GIF
frames[0].save(
    "quick_sort_animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=frame_duration,
    loop=0,
)
print("Done!")
