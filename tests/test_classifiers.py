import unittest

import ee

from eelib.classifiers import RandomForest


class TestRandomForest(unittest.TestCase):

    def test_rf_classifer_construction(self):
        rf = RandomForest(10)
        try:
            rf.classifier.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_rf_classifier_train_classifier(self):
        img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')\
            .select('B.*')

        lc = ee.Image('ESA/WorldCover/v100/2020')

        classValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
        remapValues = ee.List.sequence(0, 10)
        label = 'lc'

        lc = lc.remap(classValues, remapValues).rename(label).toByte()

        roi = ee.Geometry.Rectangle(-122.347, 37.743, -122.024, 37.838)

        sample = img.addBands(lc).stratifiedSample(**{
            'numPoints': 100,
            'classBand': label,
            'region': roi,
            'scale': 10,
            'geometries': True
        })

        sample = sample.randomColumn()
        trainingSample = sample.filter('random <= 0.8')
        validationSample = sample.filter('random > 0.8')

        rf = RandomForest(10)
        rf.train(
            featues=trainingSample,
            class_label=label,
            predictors=img.bandNames()
        )

        try:
            rf.model.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")

    def test_apply_rf_model_to_image(self):
        img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')\
            .select('B.*')

        lc = ee.Image('ESA/WorldCover/v100/2020')

        classValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
        remapValues = ee.List.sequence(0, 10)
        label = 'lc'

        lc = lc.remap(classValues, remapValues).rename(label).toByte()

        roi = ee.Geometry.Rectangle(-122.347, 37.743, -122.024, 37.838)

        sample = img.addBands(lc).stratifiedSample(**{
            'numPoints': 100,
            'classBand': label,
            'region': roi,
            'scale': 10,
            'geometries': True
        })

        sample = sample.randomColumn()
        trainingSample = sample.filter('random <= 0.8')
        validationSample = sample.filter('random > 0.8')

        rf = RandomForest(10)
        rf.train(
            featues=trainingSample,
            class_label=label,
            predictors=img.bandNames()
        )

        classified = img.classify(rf.model)

        try:
            classified.getInfo()
        except Exception as e:
            print(e)
            self.fail("band not created")
