import unittest

import ee

from eelib import deriv
from eelib.ee_data_struct import images as i


class TestOpticalDerriv(unittest.TestCase):
    xy = [-77.30685465171965, 44.03884259332009]
    point = ee.Geometry.Point(xy)

    test_opt_image: ee.Image = i.S2TOA().\
        filterDate('2018-04-01', '2018-10-31').\
        filterBounds(point).\
        first()

    def test_savi_band_creation(self):
        savi_band = deriv.SAVI(self.test_opt_image)

        try:
            savi_band.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_tassel_cap_band_creation(self):
        tassel_cap_bands = deriv.TasselCap(self.test_opt_image)

        try:
            tassel_cap_bands.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_ndvi_band_creation(self):
        ndvi_band = deriv.NDVI(self.test_opt_image)

        try:
            ndvi_band.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")


class TestSARDeriv(unittest.TestCase):
    xy = [-77.30685465171965, 44.03884259332009]
    point = ee.Geometry.Point(xy)

    test_sar_collection = i.S1().\
        filterBounds(point).\
        filterDate('2018-04-01', '2018-10-31').\
        first()

    def test_ratio_band_creation(self):
        ratio_band = sar.Ratio(
            image=self.test_sar_collection,
            numerator='VV',
            denominator='VH'
        )

        try:
            ratio_band.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")


class TestElevationDeriv(unittest.TestCase):

    def test_slope_band_creation(self):
        pass
