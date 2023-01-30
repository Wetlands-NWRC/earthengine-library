import os
import unittest

import ee
import pandas as pd

from eelib.scripttools import eemoa, extract_by_rank, plot_moa_dis

CURRENT_DIS = os.path.abspath(os.path.dirname(__file__))

class TestMoa(unittest.TestCase):

    def test_moa_tools(self):
        image = ee.Image(
            'users/ryangilberthamilton/BC/williston/stacks/WillistonA_2018')
        label_column = 'cDesc'
        pts = ee.FeatureCollection(
            'users/ryangilberthamilton/BC/williston/fpca/willistonA_no_floodplain')

        moa_table = eemoa(
            image=image,
            label_col=label_column,
            pts=pts
        )

        self.fail(moa_table.first().getInfo())

    def test_moa_extract_bands(self):
        os.chdir(CURRENT_DIS)
        
        moa_csv = "../testing_data/moa_script_tool_test.csv"
        scores_csv = "../testing_data/Samples-Test.csv"
        
        df_moa = pd.read_csv(moa_csv)
        df_scores = pd.read_csv(scores_csv)
        
        RANK = 1

        try:
            predictors = extract_by_rank(df_moa, RANK)
        except Exception:
            self.fail("failed")
        
    def test_moa_plot(self):
        os.chdir(CURRENT_DIS)
        
        moa_csv = "../testing_data/moa_script_tool_test.csv"
        scores_csv = "../testing_data/Samples-Test.csv"
        
        df_moa = pd.read_csv(moa_csv)
        df_scores = pd.read_csv(scores_csv)
        
        RANK = 1
        predictors = extract_by_rank(df_moa, RANK)
        try:
            plot_moa_dis(
                predictors=predictors,
                sample_table=df_scores,
                dir="../testing_data/plotting"
            )
        except Exception:
            self.fail("Failed")