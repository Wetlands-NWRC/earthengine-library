from typing import List, Union

import ee
import geopandas as gpd


class FeatureCollection(ee.FeatureCollection):

    def __init__(self, args, opt_column=None):
        super().__init__(args, opt_column)

    @classmethod
    def from_dataframe(cls, dataframe: gpd.GeoDataFrame):
        return cls(dataframe.__geo_interface__)

    @classmethod
    def from_file(cls, filename, layer: str = None, driver: str = None):
        gdf = gpd.read_file(
            filename=filename,
            driver=driver,
            layer=layer
        ).to_crs(4326)

        return cls(gdf.__geo_interface__)

    @classmethod
    def from_image_collection(cls, image_collection: ee.ImageCollection):
        raise NotImplementedError


class _eeImages(ee.ImageCollection):
    def __init__(self, args):
        super().__init__(args)


class S1Collection:
    __COLLECTION_ID = "COPERNICUS/S1_GRD"

    def __new__(cls) -> _eeImages:
        return _eeImages(cls.__COLLECTION_ID)


class S2TOACollection:
    __COLLECTION_ID = "COPERNICUS/S2_HARMONIZED"

    def __new__(cls) -> _eeImages:
        return _eeImages(cls.__COLLECTION_ID)


class S2SRCollection:
    __COLLECTION_ID = "COPERNICUS/S2_SR_HARMONIZED"

    def __new__(cls) -> _eeImages:
        return _eeImages(cls.__COLLECTION_ID)


class Stack(ee.Image):
    def __init__(self, images: List[Union[ee.Image, str]]):
        super().__init__(images)
        self._channel_log = None

    @property
    def channel_log(self) -> ee.FeatureCollection:
        """The channel_log property."""
        bandNames = self.bandNames()
        index = ee.List.sequence(0, bandNames.size().subtract(1))

        zipped = bandNames.zip(index)

        def format(element) -> ee.Feature:
            obj = ee.List(element)
            channel_name = ee.String(obj.get(0))
            index = ee.Number(obj.get(1))
            channel_idx = ee.String('Channel: ').cat(index.add(1).
                                                     format('%02d'))
            return ee.Feature(None, {'00_index': index,
                                     '01_Channel_index': channel_idx,
                                     '02_Channel_name': channel_name})

        features = zipped.map(format)
        return ee.FeatureCollection(features)
