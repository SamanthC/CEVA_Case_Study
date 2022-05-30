import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from imblearn.pipeline import Pipeline

from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


class Model:
    def __init__(self, name, estimator, hyperparam):
        self.name = name
        self.estimator = estimator
        self.hyperparam = hyperparam
        

    def choose_best_params(self, X, y):
        
        pipeline = Pipeline([
            ("resampling", RandomUnderSampler()),
            ("rescale", StandardScaler()),
            (self.name, self.estimator)
        ])

        grid_search = GridSearchCV(estimator = pipeline, param_grid = self.hyperparam, cv = StratifiedKFold(5))
        grid_search.fit(X, y)
        
        self.estimator = grid_search

        






