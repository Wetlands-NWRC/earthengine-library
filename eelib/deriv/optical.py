import ee


class NDVI:

    def __new__(cls, image: ee.Image, NIR: str = None, RED: str = None):
        """Band Mappings default to Sentinel - 2. Used to construct a new
        ee.Image that represents a NDVI ouput.

        Args:
            image (ee.Image): _description_
            NIR (str, optional): the NIR Band. Defaults to B8.
            RED (str, optional): The Red band. Defaults to B4.
        """
        NIR = 'B8' if NIR is None else NIR
        RED = 'B4' if RED is None else NIR

        return image.normalizedDifference([NIR, RED]).rename('NDVI')
