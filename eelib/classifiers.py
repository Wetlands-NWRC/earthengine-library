from typing import List

import ee


class RandomForest:
    def __init__(self, n_trees: int, var_per_split: int = None,
                 min_leaf_pop: int = 1, bag_frac: float = 0.5,
                 max_modes: int = None, seed: int = 0) -> None:

        self._cfg = {
            'numberOfTrees': n_trees,
            'variablesPerSplit': var_per_split,
            'minLeafPopulation': min_leaf_pop,
            'bagFraction': bag_frac,
            'maxNodes': max_modes,
            'seed': seed
        }

        self._classifier = ee.Classifier.smileRandomForest(
            **self._cfg
        )

        self._model = None
        self._output_mode = 'CLASSIFICATION'

    @property
    def classifier(self):
        """The classifier property."""
        return self._classifier

    @property
    def model(self):
        """model property, contains the trained model, if the train method
        has not been called will be set to None"""
        return self._model

    @property
    def output_mode(self):
        """The output_mode property."""
        return self._output_mode

    @output_mode.setter
    def output_mode(self, mode: str):
        self._output_mode = mode

    def train(self, featues: ee.FeatureCollection, class_label: str,
              predictors: List[str]) -> None:
        self._model = self._classifier.setOutputMode(self._output_mode)\
            .train(**{
                'features': featues,
                'classProperty': class_label,
                'inputProperties': predictors
            })
        return None
