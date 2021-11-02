from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("diploma.png")

title_font = ImageFont.truetype('arial.ttf', 50)

title_text = input("Please, input your name:")

image_editable = ImageDraw.Draw(my_image)

image_editable.text((177,500), title_text, (127, 0, 255), font=title_font)

my_image.show()
# my_image.save("result.jpg")