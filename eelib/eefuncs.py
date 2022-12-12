from typing import List, Union

import ee

from eelib import deriv, sf


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


def batch_co_register(images: List[ee.Image], max_offset: float,
                      patch_width: float = None, stiffness: float = 5.0):
    """Pops the image at index one. This is the reference image that all other
    images will be referenced to. iterates over each image in the defined image
    list applying the eefuncs.co_register function to each image.

    Args:
        images (List[ee.Image]): _description_
        max_offset (float): _description_
        patch_width (float, optional): _description_. Defaults to None.
        stiffness (float, optional): _description_. Defaults to 5.0.
    """
    ref_image = images.pop(0)
    imgs = [co_register(i, ref_image, max_offset, patch_width, stiffness) for
            i in images]
    imgs.insert(0, ref_image)
    return imgs


def batch_despeckle(images: List[ee.Image], filter: sf.Boxcar):
    """applys a spatial filter to each image in the image list. Only works on
    list of images. Not Image Collection. If using image collection use the 
    eefuncs.despeckle function.

    Args:
        images (List[ee.Image]): _description_
        filter (sf.Boxcar): _description_

    Returns:
        _type_: _description_
    """
    return [despeckle(i, filter) for i in images]


def batch_create_ratio(images: List[ee.Image], numerator: str, denominator: str) -> List[deriv.Ratio]:
    return [deriv.Ratio(img, numerator, denominator) for img in images]


def batch_create_ndvi(images: List[ee.Image], nir: str = None, red: str = None) -> List[deriv.NDVI]:
    return [deriv.NDVI(img, NIR=nir, RED=red) for img in images]


def batch_create_savi(images: List[ee.Image], nir: str = None, red: str = None,
                      coef: float = 0.5) -> List[deriv.SAVI]:
    return [deriv.SAVI(image=img, NIR=nir, RED=red, coef=coef) for img in images]
