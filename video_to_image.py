import cv2


def convert_video_to_image(upload_loc, video, video_type, image_loc):
    vid = cv2.VideoCapture(upload_loc + video + video_type)
    fps = vid.get(cv2.CAP_PROP_FPS)
    frame_num = 0

    # puts each frame to a .png file
    ret, frame = vid.read()
    while ret:
        name = image_loc + video + "-frame" + str(frame_num) + ".png"
        cv2.imwrite(name, frame)
        ret, frame = vid.read()
        frame_num += 1
    vid.release()
    cv2.destroyAllWindows()
    return fps
