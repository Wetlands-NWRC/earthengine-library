import unittest
from pprint import pprint

import ee

from eelib import sf


class TestEESpatialFilters(unittest.TestCase):

    def test_boxcar_filter_construction(self):
        eeBoxcar = sf.Boxcar(1)

        try:
            pprint(eeBoxcar.getInfo())
        except ee.EEException as e:
            print(e)
            self.fail("Something went wrong")
