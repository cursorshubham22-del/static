from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return "I am Palak!!!!"

@app.route('/sales/all')
def salesAll():
    return '{"month":"Sep","amount":1000000}'


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = [
        {"id": 1, "name": "Alice", "role": "Sales Executive", "region": "North"},
        {"id": 2, "name": "Bob", "role": "Account Manager", "region": "West"},
        {"id": 3, "name": "Charlie", "role": "Sales Manager", "region": "South"},
    ]
    return jsonify(employees)


@app.route('/sales', methods=['GET'])
def get_all_sales():
    sales = [
        {"id": 101, "employee_id": 1, "amount": 50000, "month": "Jul"},
        {"id": 102, "employee_id": 2, "amount": 75000, "month": "Aug"},
        {"id": 103, "employee_id": 3, "amount": 100000, "month": "Sep"},
        {"id": 104, "employee_id": 1, "amount": 60000, "month": "Oct"},
    ]
    return jsonify(sales)

if __name__ == '__main__':
    app.run(debug=True, port=10000)

