from PIL import Image
import os

def resize_and_save(image_path, new_size, output_path):
    image = Image.open(image_path)
    resized_image = image.resize(new_size)
    resized_image.save(output_path)

# Specify the images and their new sizes
images = [
    {"input": "roku.png", "output": "roku_resized.png"},
    {"input": "wordcloud.png", "output": "wordcloud_resized.png"},
    {"input": "comish.png", "output": "comish_resized.png"},
    {"input": "keytube.png", "output": "keytube_resized.png"},
]

new_size = (940, 650)

# Resize and save each image
for img in images:
    input_path = img["input"]
    output_path = img["output"]
    resize_and_save(input_path, new_size, output_path)

print("Images resized and saved to the same directory.")
