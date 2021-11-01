from flask import Flask
from flask import request
from flask import jsonify

import xgboost as xgb
import pickle

print(xgb.__version__)

model_file = 'model_I_xgb.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('income')    

@app.route('/heartbeat',methods = ['GET'])
def heartbeat():
    return 'up!'

@app.route('/predict', methods=['POST'])
def predict():
    person = request.get_json()

    X = dv.transform([person])
    model_features = model.feature_names
    dval = xgb.DMatrix(X, feature_names=model_features)
    y_pred = model.predict(dval, ntree_limit=model.best_iteration)

    print()

    result = {
        'income_up_to_50K_probability': float(y_pred)
    }

    return jsonify(result)    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
