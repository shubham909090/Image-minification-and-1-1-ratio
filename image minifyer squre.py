from PIL import Image
import os

input_dir = 'Python\image minify\large'
output_dir = 'Python\image minify\mini'

for filename in os.listdir(input_dir):
    if filename.endswith(('jpg', 'png', 'jpeg')):
        img = Image.open(os.path.join(input_dir, filename))
        max_size = 1080
        if img.size[0] > img.size[1]:
            height = max_size
            width = int(max_size * img.size[0] / img.size[1])
        else:
            width = max_size
            height = int(max_size * img.size[1] / img.size[0])
        img = img.resize((width, height), Image.ANTIALIAS)
        left = (width - max_size)/2
        top = (height - max_size)/2
        right = (width + max_size)/2
        bottom = (height + max_size)/2
        img = img.crop((left, top, right, bottom))
        base_filename, file_extension = os.path.splitext(filename)
        new_filename = base_filename + '.webp'
        img.save(os.path.join(output_dir, new_filename), 'webp')
