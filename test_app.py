import unittest
import base64
import io
from PIL import Image
import numpy as np
from app import app, expressions

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_process_image(self):
        # Load the image
        with open('Validation/angry/Training_964885.jpg', 'rb') as f:
            image_data = f.read()

        # Encode the image as base64 string
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        # Send a POST request with the image
        response = self.app.post('/process_image', data={
            'image': f'data:image/jpeg;base64,{image_base64}'
        })

        # Verify the response status code
        self.assertEqual(response.status_code, 200)

        # Verify the response content type
        self.assertIn('application/json', response.content_type)

        # Verify the predicted expressions and probabilities
        data = response.get_json()
        self.assertEqual(set(data.keys()), set(expressions))
        self.assertAlmostEqual(sum(data.values()), 1.0, places=2)

if 'myapp' == '__main__':
    unittest.main()
