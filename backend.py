from flask import Flask, jsonify, request
from keras.models import load_model
from PIL import Image
import numpy as np, h5py

app = Flask('myapp')
model = load_model('E:\ICBT\PROJECT\Facial-Expressions-Recognition-master\model.h5')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image from the request
    file = request.files['file']
    img = Image.open(file.stream)
    
    # Preprocess the image for the model
    img = img.resize((48, 48))
    img = img.convert('L')
    img_array = np.array(img) / 255.
    img_array = img_array.reshape((1, 48, 48, 1))
    
    # Predict the emotion from the image
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    predictions = model.predict(img_array)[0]
    results = {emotions[i]: round(predictions[i] * 100, 2) for i in range(len(emotions))}
    
    return jsonify(results)

if 'myapp' == '__main__':
    app.run(debug=True)
