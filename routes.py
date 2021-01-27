from flask import Flask, render_template
from flask import request, redirect
from pytube import YouTube

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/start', methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        video_link = request.form.get('paste_link')
        try:
            yt = YouTube(video_link)
        except:
            print("Connection error")
        stream = yt.streams.first()

        return render_template('result.html')


if __name__ ==  "__main__":
    app.run(debug=True)