import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return ('The API is currently available!')
    
@app.route('/avg-salary')
def avg_salary():
    
    table = pd.read_csv('api_file.csv', sep=';')
    avarage_salary = table['EstimatedSalary'].mean()
    content = {'avg_salary':avarage_salary}
        
    return jsonify(content)

app.run(host='0.0.0.0')