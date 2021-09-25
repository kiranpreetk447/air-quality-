#importing the libraries
import pickle
import numpy
from flask import Flask, request, render_template

#Global Variables
app = Flask(__name__)
loadedModel= pickle.load(open('AirQualityUCI.pkl','rb'))

#user defined functions
@app.route("/",methods=['Get'])
def Home():
    return render_template('air.html')

#user input commands
@app.route('/prediction',methods=['POST'])
def predict():
    City=(request.form['City'])
    PT08_S1_CO=float(request.form['PT08_S1_CO'])
    PT08_S2_NMHC=float(request.form['PT08_S2_NMHC'])
    PT08_S3_Nox=float(request.form['PT08_S3_Nox'])
    PT08_S4_NO2=float(request.form['PT08_S4_NO2'])

    prediction=loadedModel.predict([[PT08_S1_CO,PT08_S2_NMHC,PT08_S3_Nox,PT08_S4_NO2]])

    if prediction >=[35.0]:
        prediction = 'Very High pollution'

    else:
        prediction = 'less pollution'

    return render_template('air.html',prediction_output = prediction)

#main function
if __name__=="__main__":
     app.run(debug=True)
