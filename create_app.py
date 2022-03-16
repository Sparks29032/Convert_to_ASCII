from flask import Flask, render_template, request, send_file
from flask_dropzone import Dropzone
from convert import *

# create path to base directory
basedir = os.path.abspath(os.path.dirname(__name__))

# create Flask app with a few directories
app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE=5,
    DROPZONE_TIMEOUT=(60 * 1000)
)

# create Dropzone
dropzone = Dropzone(app)


# define functionalities
@app.route('/', methods=['GET', 'POST'])
def make_ascii():
    if request.method == 'POST':
        # if the button is not pressed
        if request.form.get('button') != 'CONVERT!':
            # accept uploads
            f = request.files.get('file')
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

        # if the button is pressed
        if request.form.get('button') == 'CONVERT!':
            try:
                # get the scale
                scale = float(request.form['scale'])
            except ValueError:
                # default is 1/5
                scale = 1 / 5

            # convert to ascii
            convert(1 / scale)
    # template file
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
