from get_file_types import *
from image_to_txt import *
from txt_to_image import *
from video_to_image import *
from image_to_video import *


def convert(scale, is_text, w_scale):
    image_types = [".png", ".jpg", ".jpeg", ".jfif"]
    video_types = [".mp4", ".mov", ".avi"]

    # directories we've created (may be empty)
    upload_loc = 'uploads/'
    text_loc = 'text_conversions/'
    completed_loc = 'completed/'
    parsed_images_loc = 'images/'
    basedir = os.path.abspath(os.path.dirname(__name__))
    uploads = os.path.join(basedir, upload_loc)
    text_conversions = os.path.join(basedir, text_loc)
    complete = os.path.join(basedir, completed_loc)
    images = os.path.join(basedir, parsed_images_loc)
    directories = [uploads, text_conversions, complete, images]

    # subdirectories in completed
    pictures_loc = 'pictures/'
    videos_loc = 'videos/'
    raw_loc = 'text-files/'
    pictures = os.path.join(complete, pictures_loc)
    videos = os.path.join(complete, videos_loc)
    raw = os.path.join(complete, raw_loc)
    directories.extend([pictures, videos, raw])

    # ensures the directories exist
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    while len(os.listdir(uploads)) > 0:
        names, types = get_types()
        # convert pictures into ascii
        if types[0].lower() in image_types:
            if is_text:
                convert_image_to_txt(upload_loc, names[0], types[0], completed_loc + raw_loc, scale, w_scale)
                print("Finished converting image to ascii.")
                os.remove(uploads + names[0] + types[0])
            else:
                convert_image_to_txt(upload_loc, names[0], types[0], text_loc, scale, w_scale)
                print("Finished converting image to ascii.\nImage generation in process.")
                os.remove(uploads + names[0] + types[0])
                convert_txt_to_image(completed_loc + pictures_loc, text_loc, names[0])
                print("Finished creating image.")
                os.remove(text_conversions + names[0] + '.txt')
            names.pop(0)
            types.pop(0)

        # convert video into pictures then pictures all into ascii
        elif types[0].lower() in video_types:
            fps = convert_video_to_image(upload_loc, names[0], types[0], parsed_images_loc)
            print("Finished converting video to frames.")
            os.remove(uploads + names[0] + types[0])
            frames = len(os.listdir(images))

            if is_text:
                # create a subdirectory for the text files for this video
                video_files_loc = names[0] + '/'
                video_files = os.path.join(raw, video_files_loc)
                if not os.path.isdir(video_files):
                    os.mkdir(video_files)

                counter = 1
                # convert all the images into txt files
                for image in os.listdir(images):
                    num = image[image.rfind("-frame") + len("-frame"):image.rfind('.')]
                    if len(num) < len(str(frames)):
                        while len(num) < len(str(frames)):
                            num = '0' + num
                        new_name = image[:image.rfind("-frame") + len("-frame")] + num + '.jpg'
                        os.rename(images + image, images + new_name)
                        image = new_name
                    convert_image_to_txt(
                        parsed_images_loc,
                        image[:image.rfind('.')],
                        image[image.rfind('.'):],
                        upload_loc + raw_loc + video_files_loc,
                        scale,
                        w_scale
                    )
                    print("Finished converting frame", str(counter) + "/" + str(frames), "to ascii.")
                    os.remove(images + image)
                    counter += 1
            else:
                counter = 1
                # convert all the images into txt files
                for image in os.listdir(images):
                    num = image[image.rfind("-frame") + len("-frame"):image.rfind('.')]
                    if len(num) < len(str(frames)):
                        while len(num) < len(str(frames)):
                            num = '0' + num
                        new_name = image[:image.rfind("-frame") + len("-frame")] + num + '.jpg'
                        os.rename(images + image, images + new_name)
                        image = new_name
                    convert_image_to_txt(
                        parsed_images_loc,
                        image[:image.rfind('.')],
                        image[image.rfind('.'):],
                        text_loc,
                        scale,
                        w_scale
                    )
                    print("Finished converting frame", str(counter) + "/" + str(frames), "to ascii.")
                    os.remove(images + image)
                    counter += 1

                print("Video generation in process.")
                counter = 1
                # convert all the txt files into images
                for text in os.listdir(text_conversions):
                    convert_txt_to_image(parsed_images_loc, text_loc, text[:text.find('.')])
                    print("Finished creating image ", str(counter) + "/" + str(frames) + ".")
                    os.remove(text_conversions + text)
                    counter += 1

                # put all the images together in a video
                print("Creating video.")
                convert_image_to_video(completed_loc + videos_loc, images, names[0], fps)
                print("Finished creating video.")
            names.pop(0)
            types.pop(0)

        # unrecognized file type, is automatically removed
        else:
            print("Unrecognized file type.")
            os.remove(uploads + names[0] + types[0])
            names.pop(0)
            types.pop(0)
