from dataclasses import dataclass, field
from typing import List

import ee


@dataclass
class TrainingData:
    collection: ee.FeatureCollection
    samples: ee.FeatureCollection
    class_labels: str = field(init=True, repr=True, default='land_cover')
    class_values: str = field(init=True, repr=True,
                              default='land_value')
    _samples: ee.FeatureCollection = field(
        init=False, repr=False, default=None)
    _collection: ee.FeatureCollection = field(
        init=False, repr=False, default=None)

    @property
    def samples(self):
        """The samples property."""
        return self._samples

    @samples.setter
    def samples(self, value):
        if type(value) is property:
            value = TrainingData._samples
        self._samples = value

    @property
    def collection(self):
        """The collection property."""
        return self._collection

    @collection.setter
    def collection(self, value):
        if type(value) is property:
            value = TrainingData._collection
        self._collection = value


def training_samples(image: ee.Image, training_data: TrainingData,
                     properties: List[str] = None, scale: float = None,
                     tile_scale: float = 1.0, geometries: bool = False):
    test_geometry_type = training_data.collection.geometry().type().getInfo()
    if test_geometry_type != 'MultiPoint':
        raise ee.EEException("Collection is not of type MultiPoint")

    samples = image.sampleRegions(**{
        'collection': training_data.collection,
        'scale': scale,
        'tileScale': tile_scale,
        'properties': properties,
        'geometries': geometries
    })
    training_data.samples = samples
    return training_data
