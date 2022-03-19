from get_file_types import *
from video_to_image import *
from image_to_video import *
from image_to_pixel import *
import shutil


def pixelate(scale):
    image_types = [".png", ".jpg", ".jpeg", ".jfif"]
    video_types = [".mp4", ".mov", ".avi"]

    # directories we've created (may be empty)
    upload_loc = 'uploads/'
    completed_loc = 'completed/'
    parsed_images_loc = 'images/'
    basedir = os.path.abspath(os.path.dirname(__name__))
    uploads = os.path.join(basedir, upload_loc)
    complete = os.path.join(basedir, completed_loc)
    images = os.path.join(basedir, parsed_images_loc)
    directories = [uploads, complete, images]

    # clear the images directory
    if os.path.isdir(images):
        shutil.rmtree(images, ignore_errors=True)

    # subdirectories in completed
    pixelated_loc = 'pixelated/'
    pictures_loc = pixelated_loc + 'pictures/'
    videos_loc = pixelated_loc + 'videos/'
    pixelated = os.path.join(complete, pixelated_loc)
    pictures = os.path.join(complete, pictures_loc)
    videos = os.path.join(complete, videos_loc)
    directories.extend([pixelated, pictures, videos])

    # ensures the directories exist
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    while len(os.listdir(uploads)) > 0:
        names, types = get_types()
        # pixelate pictures
        if types[0].lower() in image_types:
            print("Processing image.")
            pixelate_image(upload_loc, names[0], types[0], completed_loc + pictures_loc, scale)
            print("Finished pixelating image.")
            os.remove(uploads + names[0] + types[0])
            names.pop(0)
            types.pop(0)

        # pixelate videos
        elif types[0].lower() in video_types:
            print("Processing video.")
            fps = convert_video_to_image(upload_loc, names[0], types[0], images)
            print("Finished converting video to frames.")
            os.remove(uploads + names[0] + types[0])

            # set up the pixel directory in images
            pixel_loc = "pixel/"
            pixel = os.path.join(images, pixel_loc)

            frames = len(os.listdir(images))

            # ensure no pixel directory exists
            if os.path.isdir(pixel):
                shutil.rmtree(pixel, ignore_errors=True)

            # rename images
            for image in os.listdir(images):
                num = image[image.rfind("-frame") + len("-frame"):image.rfind('.')]
                if len(num) < len(str(frames)):
                    while len(num) < len(str(frames)):
                        num = '0' + num
                    new_name = image[:image.rfind("-frame") + len("-frame")] + num + '.png'
                    os.rename(images + image, images + new_name)

            # get list of images
            image_list = os.listdir(images)

            # create directory to store pixelated images
            os.mkdir(pixel)

            counter = 1
            # convert all the images into txt files
            for image in image_list:
                pixelate_image(
                    parsed_images_loc,
                    image[:image.rfind('.')],
                    image[image.rfind('.'):],
                    parsed_images_loc + pixel_loc,
                    scale
                )
                print("Finished making frame", str(counter) + "/" + str(frames), "into pixelated version.")
                os.remove(images + image)
                counter += 1

            # put all the images together in a video
            print("Creating video.")
            convert_image_to_video(completed_loc + videos_loc, pixel, names[0], fps)
            print("Finished creating video.")
            names.pop(0)
            types.pop(0)

        # unrecognized file type, is automatically removed
        else:
            print("Unrecognized file type.")
            os.remove(uploads + names[0] + types[0])
            names.pop(0)
            types.pop(0)
