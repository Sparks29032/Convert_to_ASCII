# What it does
Creates a local server where you can upload images and videos.

These media files can then be converted to ASCII versions of themselves.

Converted images are saved to a local folder called "completed".

### References
Used MIT's "hack" font in fonts directory.


# How to use
Run create_app.py to create a local server (http://127.0.0.1:8080/).

The first time you run the local server, hit convert before uploading files -- this will create required dependencies.

Here, you can upload files to the box and hit convert to convert all uploaded files.

Conversion does take a while as pixels are translated almost 1:1.

For smaller file size, change scale to a smaller number (1/5 still provides pretty good quality).

Once conversion is finished, the uploads should disappear.

All converted files will be placed in a local folder "completed" in the same directory as create_app.py.

### Required dependencies
See requirements.txt.
