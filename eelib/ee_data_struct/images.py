import ee
import geopandas as gpd


class _eeImages(ee.ImageCollection):
    def __init__(self, args):
        super().__init__(args)

    def to_dataframe(self) -> gpd.GeoDataFrame:
        raise NotImplementedError

    def to_feature_collection(self) -> ee.FeatureCollection:
        raise NotImplementedError


class S1(_eeImages):
    __COLLECTION_ID = "COPERNICUS/S1_GRD"

    def __init__(self):
        super().__init__(self.__COLLECTION_ID)


class S2TOA(_eeImages):
    __COLLECTION_ID = "COPERNICUS/S2_HARMONIZED"

    def __init__(self):
        super().__init__(self.__COLLECTION_ID)


class S2SR(_eeImages):
    __COLLECTION_ID = "COPERNICUS/S2_SR_HARMONIZED"

    def __init__(self):
        super().__init__(self.__COLLECTION_ID)
