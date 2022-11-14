import ee


class Ratio:

    def __new__(cls, image: ee.Image, numerator: str, denominator: str):

        exp = "x / y"
        opt_map = {
            'x': image.select(numerator),
            'y': image.select(denominator)
        }

        derv = image.expression(
            expression=exp,
            opt_map=opt_map
        )

        return derv.rename('Ratio')
