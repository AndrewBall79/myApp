from PIL import Image, ImageFilter


img = Image.open('./Pokedex/astro.jpg')
img.thumbnail((400, 400))
img.save('./Pokedex/thumbnail.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# bw_img = img.convert('L')
# bw_img.save('bw.png', 'png')
