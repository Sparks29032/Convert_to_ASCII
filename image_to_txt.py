from PIL import Image


def convert_image_to_txt(upload_loc, image, image_type, text_loc, scale, w_scale):
    # open image and get specs
    im = Image.open(upload_loc + image + image_type, 'r')
    w, h = im.size
    pix = im.load()
    b_array = []

    # how large you want the image to be
    w = int(w * w_scale / scale)
    h = int(h / scale)

    # get the brightness of each section of the image
    for j in range(h):
        row = []
        for i in range(w):
            # calculated based on weightings for each RGB color
            bright = (0.299 * pix[int(i * scale / w_scale), int(j * scale)][0] +
                      0.587 * pix[int(i * scale / w_scale), int(j * scale)][1] +
                      0.114 * pix[int(i * scale / w_scale), int(j * scale)][2]) / 256
            row.append(bright)
        b_array.append(row)
    ascii_array = []

    # ascii from darkest to brightest
    gs = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`\'. "

    # replace brightness with ascii values
    for j in range(h):
        row = []
        for i in range(w):
            row.append(gs[int(len(gs) * b_array[j][i])])
        ascii_array.append(row)

    # write to txt file
    f = open(text_loc + image + '.txt', 'w')
    for j in range(h):
        line = ""
        for i in range(w):
            line += ascii_array[j][i]
        f.write(line + "\n")
    f.close()
