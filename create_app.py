from flask import Flask, render_template, request
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
        if request.form.get('a_button') != 'Convert to ASCII!' and request.form.get('p_button') != 'Pixelate!':
            # accept uploads
            f = request.files.get('file')

            # ensure there is an upload
            try:
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
            except AttributeError:
                return render_template('index.html')

        # if the button is pressed
        if request.form.get('a_button') == 'Convert to ASCII!':
            try:
                # get the scale
                scale = float(request.form['scale'])
            except ValueError:
                # default is 1/5
                scale = 1 / 5

            # check if they want only the txt files
            is_text = request.form.get('text')
            if str(is_text) == "None":
                is_text = False

                # set the width scale (default at 1.4)
                w_scale = 1.4
            else:
                is_text = True

                # allow user to choose the width scale
                w_scale = float(request.form['wideness'])

            # convert to ascii
            convert(1 / scale, is_text, w_scale)
    # template file
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
