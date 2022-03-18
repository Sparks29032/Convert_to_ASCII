# What it does
Creates a local server where you can upload images and videos. These media files can then be converted to ASCII versions of themselves. Converted images are saved to a local folder called "completed". For example, this image:

<img src="https://user-images.githubusercontent.com/59151395/158705313-ef543100-8033-4d65-bfb0-212fa7db2c30.jpg" width="1000">

Was converted into:

<img src="https://user-images.githubusercontent.com/59151395/158738309-0673c619-bbfa-48c5-b4c5-40ea7b82fbb2.png" width="1000">

Zoomed in:

<img src="https://user-images.githubusercontent.com/59151395/158738611-35d28dfd-e3d2-4fdd-a106-ce4cfb4ead26.png" width="1000">

### References
Used MIT's open-source "hack" font in fonts directory.

# How to use
Run create_app.py to create a local server (http://127.0.0.1:8080/).
The first time you run the local server, hit convert before uploading files -- this will create required dependencies.
Here, you can upload files to the box.

Then, choose a scale factor you want the output to be created in.
For larger files, a scale of 0.2 provides pretty good quality. 
You can also choose if you want the final file to be a txt file. 
If so, you can then change the wideness of the final output. 

Finally, hit convert to convert your file into ascii!
Note, 1:1 conversions usually take a pretty long time.
Once conversion is finished, the uploads should disappear.
All converted files will be placed in a local folder "completed" in the same directory as create_app.py.

### Output
For images: .png  
For videos: .mp4  
Raw output: .txt  
