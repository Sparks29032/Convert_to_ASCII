from flask import Flask, render_template, request, send_file
from flask_dropzone import Dropzone
from convert import *

# what is the pixel:character ratio you want (1/5 works pretty well)
scale = 1

# find where the app is located
basedir = os.path.abspath(os.path.dirname(__name__))

# create applet
app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    
    # max upload size is 5 Mb
    DROPZONE_MAX_FILE_SIZE=5,
    
    # at most the program waits 1 min for uplaods
    DROPZONE_TIMEOUT=(60 * 1000)
)

# create dropzone
dropzone = Dropzone(app)


# give app convert and upload functionalities
@app.route('/', methods=['GET', 'POST'])
def make_ascii():
    if request.method == 'POST':
        # if button is not pressed
        if request.form.get('button') != 'CONVERT!':
            # allows for uploads
            f = request.files.get('file')
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        
        # if button is pressed
        if request.form.get('button') == 'CONVERT!':
            # converts all items in the uploads folder
            convert(int(1 / scale))
    return render_template('index.html')


# host server
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
