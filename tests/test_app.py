import unittest
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_endpoint(self):
        # Data based on Train.csv sample
        # 9.300000, 1, 0.016047, 4, 249.809204, 1999, 1, 0, 1
        data = {
            'item_weight': '9.3',
            'item_fat_content': '1',
            'item_visibility': '0.016047',
            'item_type': '4',
            'item_mrp': '249.8092',
            'outlet_establishment_year': '1999',
            'outlet_size': '1',
            'outlet_location_type': '0',
            'outlet_type': '1'
        }

        response = self.app.post('/predict', data=data)

        self.assertEqual(response.status_code, 200)
        # Check if the response contains the prediction result
        self.assertIn(b'Predicted Item Outlet Sales:', response.data)


if __name__ == '__main__':
    unittest.main()
