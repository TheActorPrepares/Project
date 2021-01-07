from flask import Flask,request
import pandas as pd
import numpy as np
import flasgger
from flasgger import Swagger
import pickle
#To start flask app
#step1
app=Flask(__name__)
Swagger(app)
# print(__name__)
pickle_in=open('Adv.pkl','rb')
Ecom=pickle.load(pickle_in)


@app.route('/')
def FlipKart():
    return 'Welcome to FlipKart'

@app.route('/predict',methods=["GET"])
def predict_yearly_spent():

    """Let's Authenticate the Banks Note
        This is using docstrings for specifications.
    ---
    parameters:
      - name: Daily Time Spent on Site
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: Area Income
        in: query
        type: number
        required: true
      - name: Daily Internet Usage
        in: query
        type: number
        required: true
      - name: Male
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    Daily_Time_Spent=request.args.get('Daily Time Spent on Site')
    Age=request.args.get('Age')
    Area_Income=request.args.get('Area Income')
    Internet_Usage=request.args.get('Daily Internet Usage')
    Gender=request.args.get('Male')
    prediction=Ecom.predict([[Daily_Time_Spent,Age,Area_Income,Internet_Usage,Gender]])
    return "Clicked on Ad is  "+ str(prediction)

#step1  app will get run
if __name__=='__main__':
    app.run()
