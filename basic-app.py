from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

app = FastAPI()

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
    
# @app.get('/')
# def main():
#     return {'message': 'Welcome to IndiaGate!!!'}

# @app.get('/{name}')
# def hello_name(name: str):
#     return {'message': f'Welcome to INDIAGATE!, {name}'}

iris = load_iris()

X = iris.data
Y = iris.target

clf = GaussianNB()
clf.fit(X, Y)


@app.post('/predict')
def predict(data: request_body):
    test_data = [[
        data.sepal_length, 
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    
    class_idx = clf.predict(test_data)[0]
    
    return {'class' : iris.target_names[class_idx]}