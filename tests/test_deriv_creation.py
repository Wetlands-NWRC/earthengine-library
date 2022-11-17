import unittest

import ee

from eelib.deriv import optical as opt
from eelib.ee_data_struct import images as i


class TestOpticalDerriv(unittest.TestCase):
    xy = [-77.30685465171965, 44.03884259332009]
    point = ee.Geometry.Point(xy)

    test_opt_image: ee.Image = i.S2TOA().\
        filterDate('2018-04-01', '2018-10-31').\
        filterBounds(point).\
        first()

    def test_savi_band_creation(self):
        savi_band = opt.SAVI(self.test_opt_image)

        try:
            savi_band.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_tassel_cap_band_creation(self):
        tassel_cap_bands = opt.TasselCap(self.test_opt_image)

        try:
            tassel_cap_bands.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_ndvi_band_creation(self):
        ndvi_band = opt.NDVI(self.test_opt_image)

        try:
            ndvi_band.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")


class TestSARDeriv(unittest.TestCase):

    def test_ratio_band_creation(self):
        pass


class TestElevationDeriv(unittest.TestCase):

    def test_slope_band_creation(self):
        pass
