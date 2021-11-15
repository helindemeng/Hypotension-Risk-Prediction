#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from main import predict_result
import traceback
from src.preprocess import *

app = Flask(__name__)
CORS(app, resources=r'/*')  # 跨域
app.config['JSON_AS_ASCII'] = False  # 返回显示中文


@app.route('/predict', methods=['POST'])
def predict():
    data = {}

    try:
        params = request.json
        print(f"接受参数: {params}")
        data = predict_result(params, df_train, estimator)

    except:
        traceback.print_exc()

    finally:
        res = {'code': 200, 'msg': 'success', 'data': data}
        print(f"返回参数: {res}\n")

        return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
