#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from src.predict import model_predict


def predict_result(user_params: dict, df_train, estimator_fit):
    """
    Args:
        user_params: 用户参数
                    X81 = (X104 / X80) * 1000，即 （尿素/肌酐）= (尿素 / 肌酐) * 1000
                    X62 和 X71 ，接收的值是 0-100 之间，需要转换成 0-1 之间
        df_train:
        estimator_fit:

    Return: 预测结果
    """
    user_params['X81'] = (user_params['X104'] / user_params['X80']) * 1000.
    user_params['X62'] = user_params['X62'] / 100.
    user_params['X71'] = user_params['X71'] / 100.

    return model_predict(user_params, df_train, estimator_fit)
