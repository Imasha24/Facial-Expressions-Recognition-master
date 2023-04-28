from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import io
import numpy as np
from PIL import Image
import tensorflow as tf

import os
import tensorflow as tf

current_dir = os.getcwd()

# Load the pre-trained model
model_dir = r'E:\ICBT\PROJECT\Facial-Expressions-Recognition-master\Model Train\model.h5'
model = tf.keras.models.load_model(model_dir)



app = Flask('myapp')
CORS(app)






# Define the list of expressions
expressions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Define a function to preprocess the image
def preprocess_image(image):
    img = image.convert('L')  # Convert to grayscale
    img = img.resize((48, 48), resample=Image.BILINEAR)  # Resize to 48x48 pixels
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Define the route to process the image
@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the image data from the request
    img_data = request.form['image'].split(',')[1]
    img_bytes = io.BytesIO(base64.b64decode(img_data))

    # Convert the image to a PIL Image object
    image = Image.open(img_bytes)

    # Preprocess the image
    img = preprocess_image(image)

    # Make a prediction with the model
    predictions = model.predict(img)

    # Format the response
    results = {expression: str(round(probability * 100, 2)) + '%' for expression, probability in zip(expressions, predictions[0])}

    # Return the response
    return jsonify(results)

if __name__ == '__main__':
    app.run()
