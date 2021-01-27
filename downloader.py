# import the library
from pytube import YouTube

# path where to save the video
path = r"C:\Users\Shri Krishan\Downloads"

# youtube link of the video

link = "https://youtu.be/m6Y8xEfyXTs?list=RDm6Y8xEfyXTs"

try:
    # object creation of the module
    yt = YouTube(link)
except:
    print("Connection error")


stream = yt.streams.first()
try:
    # downloading the video
    stream.download()
except:
    print("Some Error!")
print('Task Completed!')
