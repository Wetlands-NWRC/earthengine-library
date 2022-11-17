import ee
import geopandas as gpd


class _eeImages(ee.ImageCollection):
    def __init__(self, args):
        super().__init__(args)


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


class Stack:
    def __new__(cls, *images) -> ee.Image:
        """Constructs a New Image. Stacks all images together

        Returns:
            ee.Image: an Image that Represents a Stack of images
        """
        return ee.Image.cat(images)
