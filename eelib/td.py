from abc import ABC
from pprint import pprint
from typing import List, Union

import ee


class TrainingSample(ABC):
    pass


class TrainingSamples(TrainingSample):

    def __init__(self, image: ee.Image, collection: ee.FeatureCollection,
                 properties: List[str] = None, scale: float = None,
                 projection: ee.Projection = None, tile_scale: float = 1,
                 geometries: bool = False):
        test_geometry_type = collection.geometry().type().getInfo()
        if test_geometry_type != 'MultiPoint':
            raise ee.EEException("Collection is not of type MultiPoint")

        self._image = image
        self._collection = collection
        self._properties = properties
        self._scale = scale
        self._projection = projection
        self._tile_scale = tile_scale
        self._geometries = geometries

    def get_samples(self) -> ee.FeatureCollection:
        samples = self._image.sampleRegions(**{
            'collection': self._collection,
            'scale': self._scale,
            'tileScale': self._tile_scale,
            'projection': self._projection,
            'properties': self._properties,
            'geometries': self._geometries
        })
        return samples
