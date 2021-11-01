# Midterm project

**Income classification** 

Prediction task is to determine whether a person makes over 50K a year.

## Dataset

* [https://www.kaggle.com/lodetomasi1995/income-classification](https://www.kaggle.com/lodetomasi1995/income-classification)
* Copy of the dataset: [income_evaluation.csv](./income_evaluation.csv)

## Notebook

* Colab:https://colab.research.google.com/drive/14O27isuk8rJFNOo_srXqnHl_nuBfa6GE
* copy of the notebook here: [notebook.ipynb](./notebook.ipynb)

## TLDR; Use the API

Predict if a certain person income is up to 50K using /predict API.

Endopoint:

* https://ml-zoomcamp-midterm-project.herokuapp.com

API:

* /heartbeat
* /predict

### Predict API

```
curl --location --request POST 'https://ml-zoomcamp-midterm-project.herokuapp.com/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 45,
    "workclass": "private",
    "fnlwgt": 209642,
    "education": "masters",
    "education-num": 14,
    "marital-status": "married-civ-spouse",
    "occupation": "exec-managerial",
    "relationship": "husband",
    "race": "white",
    "sex": "male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 45,
    "native-country": "italy"
}'
```

Or download Postman collection: [Income Prediction.postman_collection.json](./Income%20Prediction.postman_collection.json)


## Run locally with docker

### Docker

```
docker build -t income-prediction ./src
docker run -it -p 9696:9696 income-prediction:latest
```


### Predict

```
curl --location --request POST 'http://localhost:9696/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 45,
    "workclass": "private",
    "fnlwgt": 209642,
    "education": "masters",
    "education-num": 14,
    "marital-status": "married-civ-spouse",
    "occupation": "exec-managerial",
    "relationship": "husband",
    "race": "white",
    "sex": "male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 45,
    "native-country": "italy"
}'
```

## Run locally without docker

Python required. For more see: [https://packaging.python.org/tutorials/installing-packages/](https://packaging.python.org/tutorials/installing-packages/).

```
pip install pipenv
pipenv install
python predict.py
```

Install libomp required by xgboot:

MacOS:

```
brew install libomp
```

Ubuntu

```
RUN apt-get update && apt-get install -y libgomp1
```


## Deploy to heroku and Run

Heroku account needed. Install heroku cli.

### Docker file

Update docker file:

```
#ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"] 
ENTRYPOINT ["gunicorn", "predict:app"]
```


### login

```
heroku login
heroku container:login
```

### create app in heroku

```
heroku create your-app-name
```

### Push docker image to Heroku

```
heroku container:push web -a your-app-name
```

### Deploy container on Heroku

```
heroku container:release web -a your-app-name
```

### Launch app

Test is up: https://your-app-name-xyz.herokuapp.com/heartbeat

### Predict

Consume /predict API:

```
curl --location --request POST 'http://ml-zoomcamp-midterm-project.herokuapp.com/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 45,
    "workclass": "private",
    "fnlwgt": 209642,
    "education": "masters",
    "education-num": 14,
    "marital-status": "married-civ-spouse",
    "occupation": "exec-managerial",
    "relationship": "husband",
    "race": "white",
    "sex": "male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 45,
    "native-country": "italy"
}'
```

## Postman collection

Download postman collection

* [Income Prediction.postman_collection.json](./Income%20Prediction.postman_collection.json)

and import it in your postman account to run it.