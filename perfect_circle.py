#THIS IS CODE TO CHEAT https://neal.fun/perfect-circle/

# import the necessary packages
import imutils
import cv2
import pyautogui
import numpy as np
import math
import time

time.sleep(3)

# Grab screen cap
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find circles in the image
circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=20, minRadius=0, maxRadius=0
)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    center_screen = (image.shape[1] // 2, image.shape[0] // 2)  # Center of the screen

    # Find the closest circle center to the center of the screen
    closest_circle = min(circles, key=lambda c: abs(c[0] - center_screen[0]) + abs(c[1] - center_screen[1]))

    # Draw the circle and its center on the image
    cv2.circle(image, (closest_circle[0], closest_circle[1]), closest_circle[2], (0, 255, 0), 2)
    cv2.circle(image, (closest_circle[0], closest_circle[1]), 2, (0, 0, 255), 3)

    # Define parameters for circular movement
    center = (closest_circle[0], closest_circle[1])
    radius = closest_circle[2] * 20  # Scale up the radius

    # Perform circular mouse drag
     # Press and hold the left mouse button
    for i in range(0, 360, 12):
        x = int(center[0] + radius * math.cos(i * math.pi / 180.0))
        y = int(center[1] + radius * math.sin(i * math.pi / 180.0))
        pyautogui.moveTo(x, y, duration=0.00000000001)  # Move to the next coordinate
        pyautogui.mouseDown(button='left')

    pyautogui.mouseUp(button='left')  # Release the left mouse button

    # Show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
else:
    print("No circles found.")



