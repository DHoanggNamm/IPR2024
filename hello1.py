from PIL import Image, ImageDraw
import random

# Create a blank image with a white bg
width, height = 1000, 100
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Generate and test random pixels
for _ in range(10000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.point((x, y), fill=color)

# Save the image
image.save("test_img_pillow.png")