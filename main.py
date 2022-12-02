from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import joblib
import numpy as np
import traceback

app = Flask(__name__)
CORS(app)
model = joblib.load('modelfake.pkl')


def predict(data):
    fields = ['latitude', 'longitude', 'age_of_driver', 'vehicle_type', 'age_of_vehicle', 'engine_capacity_cc',
              'day_of_week', 'weather_conditions', 'road_surface_conditions', 'light_conditions', 'sex_of_driver', 'speed_limit']

    data = pd.DataFrame({v: [data[v]] for v in fields}).reset_index(drop=True)
    print(data.shape)

    try:
        result = model.predict(data[fields])
    except Exception as e:
        print(traceback.format_exc())
        result = str(e)

    return str(result[0])


def response_with(code, value=None,
                  headers={}):
    result = {}

    if value:
        result.update(value)

    headers.update({'Acess-Control-Allow-Origin': '*'})
    headers.update({'server': 'SENAP API'})

    return make_response(jsonify(result), code, headers)


@app.route('/', methods=['GET'])
def index():
    return "HELLO FROM SERVER"

# API MAIN ENDPOINT


@app.route('/api/predict', methods=['POST'])
def pred():
    try:
        res = predict(request.get_json())
        return response_with(200, value={'msg': res})
    except Exception:
        return response_with(500, value={'msg': 'Erreur Prediction'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
