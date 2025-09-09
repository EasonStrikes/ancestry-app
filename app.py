from flask import Flask, request, jsonify, render_template
from deepface import DeepFace
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file.save('upload.jpg')
    result = DeepFace.analyze('upload.jpg', actions=['race'])
    return jsonify(result[0]['race'])

if __name__ == '__main__':
    app.run(debug=True)