import sys
import os
from PIL import Image

# grab args
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# check if folder exists
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print("Dir created")

for filename in os.listdir(image_folder):
    print(filename)
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{filename}.png', 'png')
    print('All done')
    # checking if it is a file
else:
    print("Directory Already Exists")

# loop through folder convert img to png
# and save to new folder


# img = Image.open('./Pokedex/astro.jpg')
# img.thumbnail((400, 400))
# img.save('./Pokedex/thumbnail.png')
# filtered_img = img.filter(ImageFilter.BLUR)
# bw_img = img.convert('L')
# bw_img.save('bw.png', 'png')
