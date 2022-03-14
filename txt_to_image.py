from PIL import Image, ImageFont, ImageDraw


def convert_txt_to_image(completed_loc, text_loc, name):
    # prints at font size 21 (pretty big)
    font_size = 21
    w_conversion = 0.57023546338
    h_conversion = 0.77380952381
    f = open(text_loc + name + '.txt', 'r')
    width = 0
    lines = []

    # calculates the height and width needed to hold everything
    for line in f:
        width = max(len(line), width)
        lines.append(line)
    width *= (w_conversion * font_size)
    width = int(width + 0.5)
    height = int(len(lines) * h_conversion * font_size + 0.5)

    # makes a new image with the proper size
    im = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('fonts/Hack-Regular.ttf', font_size)
    idx = 0

    # prints the text onto the images
    for line in lines:
        draw.text((0, int((font_size * h_conversion) * idx)), line, fill='black', font=font, align='left')
        idx += 1
    im.save(completed_loc + name + '.png')
