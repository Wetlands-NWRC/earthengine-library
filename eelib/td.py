from abc import ABC
from typing import List, Union

import ee


class TrainingSample(ABC):
    pass


class TrainingPointSamples(TrainingSample):

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

        self._training_samples = None

    def sample(self) -> None:
        self._training_samples = self._image.sampleRegions(**{
            'collection': self._collection,
            'properties': self._properties,
            'scale': self._scale,
            'projection': self._projection,
            'tileScale': self._tile_scale,
            'geometries': self._geometries
        })
        return None

    def get_trianing_samples(self) -> Union[None, ee.FeatureCollection]:
        return self._training_samples
