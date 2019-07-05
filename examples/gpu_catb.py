#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-Python.
# @File         : gpu_catb
# @Time         : 2019-07-04 13:27
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from catboost import CatBoostClassifier
from sklearn.datasets import make_classification

X, y = make_classification(100000)

model = CatBoostClassifier(loss_function="Logloss",
                           eval_metric="AUC",
                           task_type="GPU",
                           learning_rate=0.05,
                           iterations=10000,
                           l2_leaf_reg=50,
                           random_seed=666,
                           od_type="Iter",
                           depth=5,
                           early_stopping_rounds=100,
                           border_count=64,
                           has_time=True
                           )

model.fit(X, y, eval_set=(X, y), verbose=1000, use_best_model=True, plot=True)
