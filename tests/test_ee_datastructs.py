import unittest
from pprint import pprint

import ee
import geopandas as gpd

from eelib.ee_data_struct import features as f
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


class TestEEFeatureCollection(unittest.TestCase):

    def test_normal_feature_collection_construction(self):
        """ test construction """

        features = [ee.Feature(None, {'feat_idx': f'feat_{i}'})
                    for i in range(0, 3)]

        col = f.FeatureCollection(features)

        try:
            pprint(col.first().getInfo())
        except ee.EEException as e:
            print(e)
            self.fail("Something went wrong")

    def test_construct_feature_collection_from_file(self):
        file_name = "/home/hammy97/programming/remotes/earthengine-library/tests/test_data/envelope.shp"
        driver = "ESRI Shapefile"

        fc = f.FeatureCollection.from_file(
            filename=file_name,
            driver=driver
        )

        try:
            pprint(fc.first().getInfo())
        except ee.EEException as e:
            print(e)
            self.fail("Something went wrong")

    def test_construction_freature_collection_from_dataframe(self):
        from shapely.geometry import Point
        d = {'col1': ['name1', 'name2'],
             'geometry': [Point(1, 2), Point(2, 1)]}
        gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

        fc = f.FeatureCollection.from_dataframe(gdf)

        try:
            pprint(fc.first().getInfo())
        except ee.EEException as e:
            print(e)
            self.fail("Something went wrong")

    def test_construction_feature_collection_from_FileGDB_layer(self):
        file_name = "/home/hammy97/programming/remotes/earthengine-library/tests/test_data/bc_priority_areas.gdb"
        driver = "FileGDB"
        layer = "envelope"

        fc = f.FeatureCollection.from_file(
            filename=file_name,
            driver=driver,
            layer=layer
        )

        try:
            pprint(fc.first().getInfo())
        except ee.EEException as e:
            print(e)
            self.fail("Something went wrong")
