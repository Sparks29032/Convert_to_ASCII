from flask import Flask, render_template, request, send_file
from flask_dropzone import Dropzone
from convert import *

scale = 1

basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    COMPLETED_PATH=os.path.join(basedir, 'completed'),
    DROPZONE_MAX_FILE_SIZE=5,
    DROPZONE_TIMEOUT=(60 * 1000)
)

dropzone = Dropzone(app)


@app.route('/', methods=['GET', 'POST'])
def make_ascii():
    if request.method == 'POST':
        if request.form.get('button') != 'CONVERT!':
            f = request.files.get('file')
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        if request.form.get('button') == 'CONVERT!':
            convert(int(1 / scale))
    return render_template('index.html')


@app.route('/<filename>')
def download(filename):
    filename = os.path.join(app.root_path, filename)
    return send_file(filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
