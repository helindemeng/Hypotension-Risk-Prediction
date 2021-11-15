#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
配置文件
"""

LABEL_LOC: int = 0  # 数据集标签位置
DATA_LOC: int = 1  # 数据集数据起始位置
HEADER: int = 0  # 数据集的表头位置

# 多个待预测内容使用的模型id和数据路径
# 如果是集成学习模型，在 model 中填写多个模型参数
MODEL_AND_DATA_PATH: dict = {
    'probability':
        {
            'model':
                {
                    16: {'gamma': 0.2, 'max_depth': 8, 'subsample': 1.0}
                },

            # 训练集路径, 支持 .xls, .xlsx, .csv 格式, .csv用逗号 , 分割
            'datasets_path': 'data/imputing_0_手动删除X3和X976.csv'
        }
}
