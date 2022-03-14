import os
import cv2


def convert_image_to_video(completed_loc, images, video, fps):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    # calculate the maximum width and height needed for a frame
    width = 0
    height = 0
    for image in os.listdir(images):
        h, w, layer = cv2.imread(images + image).shape
        width = max(width, w)
        height = max(height, h)

    # create a video by adding each frame in
    writer = cv2.VideoWriter(completed_loc + video + '.mp4', fourcc, fps, (width, height))
    for image in os.listdir(images):
        writer.write(cv2.imread(images + image))
        os.remove(images + image)
    writer.release()
