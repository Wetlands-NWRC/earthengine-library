from typing import Union

import ee

from eelib import sf


def co_register(this_image: ee.Image, ref_image: ee.Image, max_offset: float,
                patch_width: float = None, stiffness: float = 5.0):
    """Used to register one image to the reference image"""

    return this_image.register(
        **{
            'referenceImage': ref_image,
            'maxOffset': max_offset,
            'patchWidth': patch_width,
            'stiffness': stiffness
        }
    )


def despeckle(images: Union[ee.ImageCollection, ee.Image], filter: sf.Boxcar):
    """Applys a defined spatial filter to either a single image or an image
    collection. If an image collection is passed it will apply the filter to
    every image in the Image collection

    Args:
        images (Union[ee.ImageCollection, ee.Image]): _description_
        filter (_type_): _description_
    """

    def convolve_inner(element: ee.Image) -> ee.Image:
        return element.convolve(filter)

    if isinstance(images, ee.ImageCollection):
        return images.map(convolve_inner)

    else:
        return images.convolve(filter)
