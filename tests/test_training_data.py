import unittest

import ee

from eelib import td


class TestTrainingPointSamples(unittest.TestCase):

    def test_construciton_of_training_sample_multi_point(self):
        training_data = ee.FeatureCollection(
            "users/ryangilberthamilton/BC/widgeon/3Class/wd_tr_3")
        image = ee.Image(
            "users/ryangilberthamilton/BC/widgeon/stacks/widgeon_stack_2019")

        try:
            td.TrainingPointSamples(
                image=image,
                collection=training_data,
                scale=10,
                tile_scale=16
            )
        except Exception as e:
            print(e)
            self.fail("Cannot construct Obj")

    def test_return_type_ee_FeatureCollection_true(self):
        training_data = ee.FeatureCollection(
            "users/ryangilberthamilton/BC/widgeon/3Class/wd_tr_3")
        image = ee.Image(
            "users/ryangilberthamilton/BC/widgeon/stacks/widgeon_stack_2019")

        training_ds = td.TrainingPointSamples(
            image=image,
            collection=training_data,
            scale=10,
            tile_scale=16
        )

        training_ds.sample()

        smpl = training_ds.get_trianing_samples()

        try:
            smpl.first().getInfo()
        except Exception as e:
            print(e)
            self.fail("Cannot construct Obj")
