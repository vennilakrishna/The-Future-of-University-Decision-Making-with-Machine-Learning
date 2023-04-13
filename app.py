from flask import Flask, render_template, request
import keras
from keras.models import load_model
import numpy as np


app = Flask(__name__)

model = load_model("model.h5")

@app.route('/')
def home():
	return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predicted():
    
    min1 = [290.0, 92.0, 1.0, 1.0, 1.0, 6.8, 0.0]
    max1 = [340.0, 120.0,5.0, 5.0, 5.0, 9.92, 1.0]
    k = [float(x) for x in request.form.values()]
    p=[]
    for i in range(7):
        l=(k[i]-min1[i])/(max1[i]-min1[i])
        p.append(l)
    prediction = model.predict([p])
    print(prediction)
    output=prediction[0]
    if(output==False):
        return render_template('result.html',prediction_text="You dont have a chance of getting admission.")
    else:
        return render_template('result.html',prediction_text="You have a chance of getting admission.")

if __name__ == '__main__':
	app.run(debug=True)