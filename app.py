from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

car=pd.read_csv('clean_car_dataset.csv')

@app.route('/')



def index():
    companies =sorted(car['company'].unique())
    car_models =sorted(car['Name'].unique())
    years = sorted(car['year'].unique(),reverse=True) 
    fuel_types=car['fuel_type'].unique() 

    companies.insert(0,'Select company')
    
    return render_template('index.html', companies=companies,car_models=car_models,years=years,fuel_types=fuel_types)



if __name__=='__main__':
    app.run(debug=True)