from PIL import Image, ImageFont, ImageDraw

text = input("Enter text: ")
text_font = ImageFont.truetype('verdanab.ttf', 12)
text_size = text_font.getsize(text)
text_image = Image.new('1', text_size, 255)
image_draw = ImageDraw.Draw(text_image)
image_draw.text((0, 0), text, font=text_font)

for r in range(text_size[1]):
    lines = []
    for c in range(text_size[0]):
        if text_image.getpixel((c, r)):
            lines.append(' ')
        else:
            lines.append('#')
    print(''.join(lines))