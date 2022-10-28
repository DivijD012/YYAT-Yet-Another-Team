from flask import Flask, render_template, send_from_directory
import requests

app = Flask(__name__)

url_cam = 'http://192.168.30.137/cam-hi.jpg'
url_esp = 'http://192.168.30.138/'
counter = 0

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

@app.route('/', methods=['GET'])
def root():
    global counter

    data = requests.get(url_esp).text

    image_resp = requests.get(url_cam)
    if image_resp.status_code == 200:
        counter += 1
        with open(f'images/image{counter}.jpg', 'wb') as f:
            for chunk in image_resp:
                f.write(chunk)
    
    return render_template('index.html', value=data, img_src=f'images/image{counter}.jpg')

if __name__ == '__main__':
    app.run()
