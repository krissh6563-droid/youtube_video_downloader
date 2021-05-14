from flask import Flask, render_template, request, url_for , redirect, send_file
from flask import request, redirect
from pytube import YouTube

app = Flask(__name__,
            static_url_path='/static', 
            
            )

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/fetch_url', methods=['POST', 'GET'])
def fetch_url():
    if request.method == 'POST':
        temp_url = request.form.get('url')
        url = YouTube(temp_url)
        title = url.title
        video_img = url.thumbnail_url
        
    return render_template('see_video.html', title = title , img = video_img,url = url,temp_url=temp_url)
    

@app.route('/download_video', methods = ['POST','GET'])
def download_video():
    if request.method == "POST":
        new_url = request.form.get('url')
        new_url_1 = YouTube(new_url)
        stream = new_url_1.streams.first()
        stream.download()
    return render_template('success.html')


if __name__ ==  "__main__":
    app.run(debug=True)