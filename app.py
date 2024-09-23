from flask import Flask, render_template, request, send_file
import segno
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('data')
        qr_scale= request.form.get('scale')
        # logo = request.form.get('logo')

        qr_code_path = os.path.join(app.config['UPLOAD_FOLDER'], 'qr_code.png')
        qr = segno.make(data, error='H')
        qr.save(qr_code_path,
                scale = int(qr_scale)/49)
        return send_file(qr_code_path, mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    