from PIL import Image
import os

input_dir = './large'
output_dir = './mini'

for filename in os.listdir(input_dir):
    if filename.endswith(('jpg', 'png', 'jpeg')):
        img = Image.open(os.path.join(input_dir, filename))
        max_size = (1080, 1080)
        img.thumbnail(max_size)
        base_filename, file_extension = os.path.splitext(filename)
        new_filename = base_filename + '.webp'
        img.save(os.path.join(output_dir, new_filename), 'webp')
