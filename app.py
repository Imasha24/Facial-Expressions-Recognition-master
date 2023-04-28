from flask import Flask, jsonify, request
import base64
from io import BytesIO
from PIL import Image
import numpy as np

# Import the model
from keras.models import load_model
model = load_model('model.h5')

# Define the Flask app
app = Flask('myapp')

# Define a function to preprocess the image
def preprocess_image(image_data):
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    img = img.resize((48, 48))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape((1, 48, 48, 1))
    img = img / 255.0
    return img

# Define the API route
@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image data from the POST request
    image_data = request.form['image']
    
    # Preprocess the image
    img = preprocess_image(image_data)
    
    # Make a prediction
    predictions = model.predict(img)
    labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    results = {}
    for i in range(len(labels)):
        results[labels[i]] = str(predictions[0][i])
    
    # Return the results
    return jsonify(results)

# Define the main function
if 'myapp' == '__main__':
    app.run(debug=True)
