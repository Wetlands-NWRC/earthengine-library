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
        )

        return cls(gdf.__geo_interface__)

    @classmethod
    def from_image_collection(cls, image_collection: ee.ImageCollection):
        raise NotImplementedError
