from PIL import Image, ImageDraw

image = Image.new('RGB', (800, 600), (255, 255, 0))
image.putpixel((500, 500), (0, 0, 255))

draw = ImageDraw.Draw(image)
draw.rectangle((20, 20, 200, 200), (0, 255, 0))

image.save('test_image.png')