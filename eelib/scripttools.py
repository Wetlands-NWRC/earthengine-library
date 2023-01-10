import os

from itertools import combinations
from typing import Dict, Any, Union, List

import ee
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from . import eefuncs


def eemoa(image: ee.Image, label_col: str, pts: ee.FeatureCollection) -> ee.FeatureCollection:

    def moaFeatures(list: ee.List, c1, c2):
        list = ee.List(list)
        vs_classes = f'{c1}:{c2}'

        def moaFeature(element):
            nest = ee.List(element)
            band = nest.get(0)
            value = nest.get(1)
            return ee.Feature(None, {'00_Classes': vs_classes,
                                     '02_Band': band, '03_Value': value})
        return list.map(moaFeature)

    def moaRanks(fc) -> ee.Dictionary:
        bands = fc.aggregate_array('02_Band')
        ranks = ee.List.sequence(1, bands.size())
        return ee.Dictionary.fromLists(bands, ranks)

    def instertRanks(fc, ranksLookup):
        def inner_func(element):
            band = element.get('02_Band')
            rank = ranksLookup.get(band)
            return element.set('01_Rank', rank)
        return fc.map(inner_func)

    samples = image.sampleRegions(**{
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
        c1, c2 = comb
        moa_values = eefuncs.moa_calc(
            samples=samples,
            predictors=predicts,
            label_col=label_col,
            c1=c1,
            c2=c2
        )
        features = moaFeatures(moa_values, c1, c2)
        moaFc = ee.FeatureCollection(features)
        moaSort = moaFc.sort("03_Value", False)
        rankLkup = moaRanks(moaSort)
        moaRanked = instertRanks(moaSort, rankLkup)
        collections.append(moaRanked)
    return ee.FeatureCollection(collections).flatten()


def extract_by_rank(moa_table: pd.DataFrame, rank: int = 1) -> Dict[str, pd.Series]:
    df = moa_table[moa_table['01_Rank'] == 1]
    bands = df['02_Band'].unique().tolist()
    return bands

def plot_moa_dis(predictors: List[Any], sample_table: pd.DataFrame, 
                 dir: str = None) -> None:
    
    dir = './plotting' if dir is None else dir
    
    def hist_factory(series: pd.Series, title: str, bin: Union[str, int] = None):
        bin = 'auto' if bin is None else bin
        
        n, bins, patches = plt.hist(series, bin, rwidth=0.85)

        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title(title)

        # plt.xlim(-1, 1)
        # plt.ylim(0, 700)
        maxfreq = n.max()
        plt.ylim(ymax=np.ceil(maxfreq / 100) * 100 if maxfreq % 100 
                 else maxfreq + 100)
        
        plt.grid(True)
        return n, bins, patches

    for band in predictors:
        series = sample_table[band]
        
        hist_factory(
            series=series,
            title=band,
            bin=100
        )
        if not os.path.exists(dir):
            os.makedirs(dir)

        plotname = os.path.join(dir, f'{band}.png')
        
        plt.savefig(plotname)
        plt.close()
    return None
    # Step 3: select the collection based on do lazy loading

