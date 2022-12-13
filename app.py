import flask
from flask import request
import numpy as np
import pickle

model = pickle.load(open('model/modelfinalfix.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    EXT_SOURCE_2 = float(request.form['EXT_SOURCE_2'])
    EXT_SOURCE_3 = float(request.form['EXT_SOURCE_3'])
    DAYS_EMPLOYED = int(request.form['DAYS_EMPLOYED'])
    DAYS_BIRTH = float(request.form['DAYS_BIRTH'])
    REGION_RATING_CLIENT_W_CITY = int(request.form['REGION_RATING_CLIENT_W_CITY'])
    REGION_RATING_CLIENT = int(request.form['REGION_RATING_CLIENT'])
    DAYS_CREDIT = int(request.form['DAYS_CREDIT'])
    NAME_EDUCATION_TYPE = int(request.form['NAME_EDUCATION_TYPE'])
    DAYS_LAST_PHONE_CHANGE = int(request.form['DAYS_LAST_PHONE_CHANGE'])
    DAYS_ENDDATE_FACT = int(request.form['DAYS_ENDDATE_FACT'])
    DAYS_CREDIT_ENDDATE = int(request.form['DAYS_CREDIT_ENDDATE'])
    CNT_PAYMENT = int(request.form['CNT_PAYMENT'])
    DAYS_CREDIT_UPDATE = int(request.form['DAYS_CREDIT_UPDATE'])
    CODE_GENDER = int(request.form['CODE_GENDER'])
    NAME_INCOME_TYPE = int(request.form['NAME_INCOME_TYPE'])

    predict_list = [[EXT_SOURCE_2, EXT_SOURCE_3, DAYS_EMPLOYED, DAYS_BIRTH, REGION_RATING_CLIENT_W_CITY, REGION_RATING_CLIENT, DAYS_CREDIT, NAME_EDUCATION_TYPE, DAYS_LAST_PHONE_CHANGE, DAYS_ENDDATE_FACT, DAYS_CREDIT_ENDDATE, CNT_PAYMENT, DAYS_CREDIT_UPDATE, CODE_GENDER, NAME_INCOME_TYPE]]
    
    prediction = model.predict(predict_list)
    output = {0: 'Lancar Bayar', 1: 'Gagal Bayar'}
    return flask.render_template('main.html', prediction_text='Klien teridentifikasi :  {}'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)