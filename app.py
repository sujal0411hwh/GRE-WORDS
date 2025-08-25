from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Folder to store audio files
AUDIO_FOLDER = 'static/audio'
if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)

@app.route('/')
def index():
    # List all audio files
    files = os.listdir(AUDIO_FOLDER)
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(AUDIO_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
