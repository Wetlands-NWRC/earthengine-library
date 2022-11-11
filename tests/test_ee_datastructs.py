import unittest

import ee

from eelib.ee_data_struct import images

ee.Initialize()


class TestEEImageDS(unittest.TestCase):

    def test_base_collection_type_eeImageCollection(self):
        targert = images._eeImages([ee.Image() for i in range(0, 2)])
        self.assertIsInstance(targert, ee.ImageCollection)

    def test_s1_collection_construction_get_id_(self):
        target = images.S1()
        first = target.first().get('familyName')
        second = "SENTINEL-1"
        self.assertEqual(first=first, second=second)

    def test_s2_toa_collection_get_first_image_response_dict(self):
        targert = images.S2TOA()
        first_image: ee.Image = targert.first()

        try:
            first_image.getInfo()
        except ee.EEException as e:
            print(e)
            self.fail("Could not get the response from EE")
