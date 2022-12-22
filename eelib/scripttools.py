from itertools import combinations

import ee
import eefuncs


def moa(image: ee.Image, label_col: str, pts: ee.FeatureCollection) -> ee.FeatureCollection:

    def moaFeatures(list: ee.List, c1, c2):
        def moaFeature(element):
            nest = ee.List(element)
            band = nest.get(0)
            value = nest.get(1)
            classes = f'{c1}:{c2}'
            return ee.Feature(None, {'00_Classes': classes,
                                     '02_Band': band, '03_Value': value})
        return list.map(moaFeature)

    def moaRanks(fc) -> ee.Dictionary:
        bands = fc.aggregate_array('02_Bands')
        ranks = ee.List.sequence(1, bands.size())
        return ee.Dictionary.fromLists(bands, ranks)

    def instertRanks(fc, ranksLookup):
        def inner_func(element):
            band = element.get('02_Band')
            rank = ranksLookup.get(band)
            return element.set('01_Rank', rank)
        return fc.map(inner_func)

    samples = image.SampleRegions({
        'collection': pts,
        'tileScale': 16,
        'scale': 10,
        'properties': [label_col]
    })

    labels = pts.aggregate_array(label_col).distinct().getInfo()
    predicts = image.bandNames()
    combs = combinations(labels, 2)

    collections = []
    for comb in combs:
        moa_values = eefuncs.moa_calc(
            samples=samples,
            predictors=predicts,
            label_col=label_col,
            c1=comb[0],
            c2=comb[1]
        )
        features = moa_values.map(moaFeatures)
        moaFc = ee.FeatureCollection(features)
        moaSort = moaFc.sort("03_Value", False)
        rankLkup = moaRanks(moaSort)
        moaRanked = instertRanks(moaSort, rankLkup)
        collections.append(moaRanked)
    return ee.FeatureCollection(collections).flatten()