import ee


class Slope:

    def __new__(cls, image: ee.Image, elevation: str) -> ee.Image:
        return ee.Terrain.slope(image.select('elevation'))
