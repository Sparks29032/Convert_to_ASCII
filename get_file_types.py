import os


def get_types():
    # current directory
    basedir = os.path.abspath(os.path.dirname(__name__))

    # directory with uploads
    upload_loc = 'uploads/'

    # image name
    uploads = os.path.join(basedir, upload_loc)
    entries = os.listdir(uploads)

    # parses the entries
    names = []
    types = []
    for entry in entries:
        names.append(entry[:entry.rfind('.')])
        types.append(entry[entry.rfind('.'):])

    return names, types
