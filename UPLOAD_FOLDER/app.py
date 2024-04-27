from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' 
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) 

@app.route('/upload', methods=['GET', 'POST']) 
def upload_image():
    if request.method == 'POST': 
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath) 

        return jsonify({'message': 'Image uploaded successfully'}), 200 
    else: 
        return "This is the GET /upload endpoint" 

if __name__ == '__main__':
    app.run(debug=True) 
