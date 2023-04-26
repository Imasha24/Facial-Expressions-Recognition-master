import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

# Load the pre-trained model
model = load_model('Expression_kid_vgg.h5')

# Load an image to test
img_path = 'baby.jpg'
img = image.load_img(img_path, target_size=(224, 224))

# Convert the image to an array
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Use the model to predict the facial expression in the image
preds = model.predict(x)
print(preds)

 