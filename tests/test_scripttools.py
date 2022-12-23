import unittest

import ee

from eelib.scripttools import moa


class TestMoa(unittest.TestCase):

    def test_moa_tools(self):
        image = ee.Image(
            'users/ryangilberthamilton/BC/williston/stacks/WillistonA_2018')
        label_column = 'cDesc'
        pts = ee.FeatureCollection(
            'users/ryangilberthamilton/BC/williston/fpca/willistonA_no_floodplain')

        moa_table = moa(
            image=image,
            label_col=label_column,
            pts=pts
        )

        self.fail(moa_table.first().getInfo())
