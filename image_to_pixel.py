from PIL import Image, ImageDraw


def pixelate_image(input_loc, image_name, image_type, output_loc, scale):
    # open image and define dimensions
    original = Image.open(input_loc + image_name + image_type, 'r')
    w, h = original.size
    w = int(w * scale)
    h = int(h * scale)
    size = 1 / scale
    pix = original.load()

    # create output image
    new = Image.new(mode="RGB", size=(int(w * size), int(h * size)))
    draw_new = ImageDraw.Draw(new)

    # draw each pixel of the image
    for j in range(h):
        for i in range(w):
            # store the RGB averages
            color = [0, 0, 0]

            # how large each pixel is
            box_size = (int((j + 1) * size) - int(j * size)) * (int((i + 1) * size) - int(i * size))

            # get the average color in the pixel
            for y in range(int(j * size), int((j + 1) * size)):
                for x in range(int(i * size), int((i + 1) * size)):
                    for code in range(3):
                        color[code] += pix[x, y][code]
            for code in range(3):
                color[code] = int(color[code] / box_size)

            # draw the pixel
            draw_new.rectangle(((int(i * size), int(j * size)), (int((i + 1) * size), int((j + 1) * size))),
                               fill=(color[0], color[1], color[2]))

    # save the image
    new.save(output_loc + image_name + '.png')
