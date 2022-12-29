from abc import ABC
from typing import List, Union

import ee


# @TODO convert to dataclass
class TrainingData:
    def __init__(self, collection: ee.FeatureCollection) -> None:
        self.collection = collection
        self._label_col = 'land_cover'

    @property
    def class_labels(self):
        """The class_labels property."""
        return self._class_labels

    @class_labels.setter
    def class_labels(self, value):
        self._class_labels = value


class TrainingSample(ABC):
    pass


class TrainingSamples(TrainingSample):

    def __init__(self, image: ee.Image, training_data: TrainingData,
                 properties: List[str] = None, scale: float = None,
                 projection: ee.Projection = None, tile_scale: float = 1,
                 geometries: bool = False):
        test_geometry_type = training_data.collection.geometry().type().getInfo()
        if test_geometry_type != 'MultiPoint':
            raise ee.EEException("Collection is not of type MultiPoint")

        self._image = image
        self._collection = training_data.collection
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
