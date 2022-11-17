from typing import List

import ee


class TrainingPointSamples:

    def __new__(cls, image: ee.Image, collection: ee.FeatureCollection,
                properties: List[str], scale: float = None,
                projection: ee.Projection = None, tile_scale: float = 1,
                geometries: bool = False) -> ee.FeatureCollection:

        if not isinstance(collection.geometry(), ee.Geometry.MultiPoint):
            raise ee.EEException("Collection is not of type Multi point")

        training_samples = image.sampleRegions(**{
            'collection': collection,
            'properties': properties,
            'scale': scale,
            'projection': projection,
            'tileScale': tile_scale,
            'geometries': geometries
        })

        return training_samples

    @classmethod
    def from_file(filename):
        pass
