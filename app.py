from flask import Flask, jsonify, request
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
        {"employee_id": 1, "employee_name": "Alice Johnson", "region_id": 1, "work_email": "alice.johnson@bntc.com", "department": "Sales"},
        {"employee_id": 2, "employee_name": "Bob Smith", "region_id": 7, "work_email": "bob.smith@bntc.com", "department": "Marketing"},
        {"employee_id": 3, "employee_name": "Charlie Davis", "region_id": 9, "work_email": "charlie.davis@bntc.com", "department": "Operations"},
        {"employee_id": 4, "employee_name": "Diana Martinez", "region_id": 4, "work_email": "diana.martinez@bntc.com", "department": "HR"},
        {"employee_id": 5, "employee_name": "Ethan Brown", "region_id": 6, "work_email": "ethan.brown@bntc.com", "department": "Finance"},
        {"employee_id": 6, "employee_name": "Fiona Wilson", "region_id": 7, "work_email": "fiona.wilson@bntc.com", "department": "Sales"},
        {"employee_id": 7, "employee_name": "George Anderson", "region_id": 5, "work_email": "george.anderson@bntc.com", "department": "Marketing"},
        {"employee_id": 8, "employee_name": "Hannah Thompson", "region_id": 2, "work_email": "hannah.thompson@bntc.com", "department": "Operations"},
        {"employee_id": 9, "employee_name": "Ian Clark", "region_id": 3, "work_email": "ian.clark@bntc.com", "department": "HR"},
        {"employee_id": 10, "employee_name": "Julia Rodriguez", "region_id": 6, "work_email": "julia.rodriguez@bntc.com", "department": "Finance"},
        {"employee_id": 11, "employee_name": "Kevin Lewis", "region_id": 4, "work_email": "kevin.lewis@bntc.com", "department": "Sales"},
        {"employee_id": 12, "employee_name": "Laura Walker", "region_id": 10, "work_email": "laura.walker@bntc.com", "department": "Marketing"},
        {"employee_id": 13, "employee_name": "Michael Hall", "region_id": 1, "work_email": "michael.hall@bntc.com", "department": "Operations"},
        {"employee_id": 14, "employee_name": "Natalie Young", "region_id": 3, "work_email": "natalie.young@bntc.com", "department": "HR"},
        {"employee_id": 15, "employee_name": "Oliver King", "region_id": 8, "work_email": "oliver.king@bntc.com", "department": "Finance"},
        {"employee_id": 16, "employee_name": "Priya Patel", "region_id": 7, "work_email": "priya.patel@bntc.com", "department": "Sales"},
        {"employee_id": 17, "employee_name": "Rahul Gupta", "region_id": 5, "work_email": "rahul.gupta@bntc.com", "department": "Marketing"},
        {"employee_id": 18, "employee_name": "Sara Lee", "region_id": 7, "work_email": "sara.lee@bntc.com", "department": "Operations"},
        {"employee_id": 19, "employee_name": "Thomas Baker", "region_id": 9, "work_email": "thomas.baker@bntc.com", "department": "HR"},
        {"employee_id": 20, "employee_name": "Uma Sharma", "region_id": 1, "work_email": "uma.sharma@bntc.com", "department": "Finance"},
        {"employee_id": 21, "employee_name": "Victor Hughes", "region_id": 4, "work_email": "victor.hughes@bntc.com", "department": "Sales"},
        {"employee_id": 22, "employee_name": "Wendy Morales", "region_id": 2, "work_email": "wendy.morales@bntc.com", "department": "Marketing"},
        {"employee_id": 23, "employee_name": "Xavier Perez", "region_id": 6, "work_email": "xavier.perez@bntc.com", "department": "Operations"},
        {"employee_id": 24, "employee_name": "Yasmin Ahmed", "region_id": 3, "work_email": "yasmin.ahmed@bntc.com", "department": "HR"},
        {"employee_id": 25, "employee_name": "Zachary Clark", "region_id": 8, "work_email": "zachary.clark@bntc.com", "department": "Finance"},
        {"employee_id": 26, "employee_name": "Anita Desai", "region_id": 7, "work_email": "anita.desai@bntc.com", "department": "Sales"},
        {"employee_id": 27, "employee_name": "Brian O'Connor", "region_id": 5, "work_email": "brian.oconnor@bntc.com", "department": "Marketing"},
        {"employee_id": 28, "employee_name": "Catherine Liu", "region_id": 10, "work_email": "catherine.liu@bntc.com", "department": "Operations"},
        {"employee_id": 29, "employee_name": "Daniel Kim", "region_id": 9, "work_email": "daniel.kim@bntc.com", "department": "HR"},
        {"employee_id": 30, "employee_name": "Elena Rossi", "region_id": 2, "work_email": "elena.rossi@bntc.com", "department": "Finance"},
    ]

    # Static sales data used to compute totals per employee
    sales = [
        {
            "sale_id": 1,
            "employee_id": 6,
            "customer_id": 29,
            "region_id": 7,
            "sale_date": "2025-01-14",
            "total_amount": 400.00,
        },
        {
            "sale_id": 2,
            "employee_id": 4,
            "customer_id": 92,
            "region_id": 4,
            "sale_date": "2024-01-30",
            "total_amount": 4200.00,
        },
        {
            "sale_id": 3,
            "employee_id": 2,
            "customer_id": 43,
            "region_id": 7,
            "sale_date": "2024-06-05",
            "total_amount": 3100.00,
        },
        {
            "sale_id": 4,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-08-24",
            "total_amount": 800.00,
        },
        {
            "sale_id": 5,
            "employee_id": 16,
            "customer_id": 94,
            "region_id": 7,
            "sale_date": "2024-08-26",
            "total_amount": 5900.00,
        },
        {
            "sale_id": 6,
            "employee_id": 17,
            "customer_id": 73,
            "region_id": 5,
            "sale_date": "2024-01-30",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 7,
            "employee_id": 16,
            "customer_id": 37,
            "region_id": 7,
            "sale_date": "2024-12-17",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 8,
            "employee_id": 5,
            "customer_id": 47,
            "region_id": 6,
            "sale_date": "2024-04-22",
            "total_amount": 5500.00,
        },
        {
            "sale_id": 9,
            "employee_id": 4,
            "customer_id": 18,
            "region_id": 4,
            "sale_date": "2024-02-16",
            "total_amount": 2700.00,
        },
        {
            "sale_id": 10,
            "employee_id": 11,
            "customer_id": 17,
            "region_id": 4,
            "sale_date": "2024-12-09",
            "total_amount": 2900.00,
        },
        {
            "sale_id": 11,
            "employee_id": 13,
            "customer_id": 83,
            "region_id": 1,
            "sale_date": "2024-01-02",
            "total_amount": 8300.00,
        },
        {
            "sale_id": 12,
            "employee_id": 5,
            "customer_id": 54,
            "region_id": 6,
            "sale_date": "2024-06-02",
            "total_amount": 200.00,
        },
        {
            "sale_id": 13,
            "employee_id": 10,
            "customer_id": 23,
            "region_id": 6,
            "sale_date": "2024-02-17",
            "total_amount": 2400.00,
        },
        {
            "sale_id": 14,
            "employee_id": 12,
            "customer_id": 80,
            "region_id": 10,
            "sale_date": "2024-07-24",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 15,
            "employee_id": 5,
            "customer_id": 59,
            "region_id": 6,
            "sale_date": "2024-06-25",
            "total_amount": 6600.00,
        },
        {
            "sale_id": 16,
            "employee_id": 12,
            "customer_id": 85,
            "region_id": 10,
            "sale_date": "2024-01-02",
            "total_amount": 5700.00,
        },
        {
            "sale_id": 17,
            "employee_id": 10,
            "customer_id": 76,
            "region_id": 6,
            "sale_date": "2025-01-07",
            "total_amount": 1400.00,
        },
        {
            "sale_id": 18,
            "employee_id": 2,
            "customer_id": 32,
            "region_id": 7,
            "sale_date": "2024-05-21",
            "total_amount": 1800.00,
        },
        {
            "sale_id": 19,
            "employee_id": 8,
            "customer_id": 93,
            "region_id": 2,
            "sale_date": "2025-02-04",
            "total_amount": 700.00,
        },
        {
            "sale_id": 20,
            "employee_id": 1,
            "customer_id": 64,
            "region_id": 1,
            "sale_date": "2024-09-11",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 21,
            "employee_id": 10,
            "customer_id": 50,
            "region_id": 6,
            "sale_date": "2024-06-01",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 22,
            "employee_id": 3,
            "customer_id": 100,
            "region_id": 9,
            "sale_date": "2024-06-02",
            "total_amount": 900.00,
        },
        {
            "sale_id": 23,
            "employee_id": 19,
            "customer_id": 39,
            "region_id": 9,
            "sale_date": "2024-06-07",
            "total_amount": 4400.00,
        },
        {
            "sale_id": 24,
            "employee_id": 14,
            "customer_id": 66,
            "region_id": 3,
            "sale_date": "2024-04-06",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 25,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-09-03",
            "total_amount": 4300.00,
        },
    ]

    # Compute totals per employee
    by_id = {
        e["employee_id"]: {
            **e,
            "total_sales": 0.0,
            "deals_closed": 0,
        }
        for e in employees
    }

    for s in sales:
        emp_id = s["employee_id"]
        if emp_id in by_id:
            by_id[emp_id]["total_sales"] += s["total_amount"]
            by_id[emp_id]["deals_closed"] += 1

    result = list(by_id.values())

    # Optional filters via query params
    employee_id = request.args.get("employee_id", type=int)
    region_id = request.args.get("region_id", type=int)
    employee_name = request.args.get("employee_name", type=str)

    if employee_id is not None:
        result = [e for e in result if e["employee_id"] == employee_id]

    if region_id is not None:
        result = [e for e in result if e["region_id"] == region_id]

    if employee_name is not None:
        result = [
            e
            for e in result
            if e["employee_name"].lower() == employee_name.lower()
        ]

    return jsonify(result)


@app.route('/sales', methods=['GET'])
def get_all_sales():
    sales = [
        {
            "sale_id": 1,
            "employee_id": 6,
            "customer_id": 29,
            "region_id": 7,
            "sale_date": "2025-01-14",
            "total_amount": 400.00,
        },
        {
            "sale_id": 2,
            "employee_id": 4,
            "customer_id": 92,
            "region_id": 4,
            "sale_date": "2024-01-30",
            "total_amount": 4200.00,
        },
        {
            "sale_id": 3,
            "employee_id": 2,
            "customer_id": 43,
            "region_id": 7,
            "sale_date": "2024-06-05",
            "total_amount": 3100.00,
        },
        {
            "sale_id": 4,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-08-24",
            "total_amount": 800.00,
        },
        {
            "sale_id": 5,
            "employee_id": 16,
            "customer_id": 94,
            "region_id": 7,
            "sale_date": "2024-08-26",
            "total_amount": 5900.00,
        },
        {
            "sale_id": 6,
            "employee_id": 17,
            "customer_id": 73,
            "region_id": 5,
            "sale_date": "2024-01-30",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 7,
            "employee_id": 16,
            "customer_id": 37,
            "region_id": 7,
            "sale_date": "2024-12-17",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 8,
            "employee_id": 5,
            "customer_id": 47,
            "region_id": 6,
            "sale_date": "2024-04-22",
            "total_amount": 5500.00,
        },
        {
            "sale_id": 9,
            "employee_id": 4,
            "customer_id": 18,
            "region_id": 4,
            "sale_date": "2024-02-16",
            "total_amount": 2700.00,
        },
        {
            "sale_id": 10,
            "employee_id": 11,
            "customer_id": 17,
            "region_id": 4,
            "sale_date": "2024-12-09",
            "total_amount": 2900.00,
        },
        {
            "sale_id": 11,
            "employee_id": 13,
            "customer_id": 83,
            "region_id": 1,
            "sale_date": "2024-01-02",
            "total_amount": 8300.00,
        },
        {
            "sale_id": 12,
            "employee_id": 5,
            "customer_id": 54,
            "region_id": 6,
            "sale_date": "2024-06-02",
            "total_amount": 200.00,
        },
        {
            "sale_id": 13,
            "employee_id": 10,
            "customer_id": 23,
            "region_id": 6,
            "sale_date": "2024-02-17",
            "total_amount": 2400.00,
        },
        {
            "sale_id": 14,
            "employee_id": 12,
            "customer_id": 80,
            "region_id": 10,
            "sale_date": "2024-07-24",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 15,
            "employee_id": 5,
            "customer_id": 59,
            "region_id": 6,
            "sale_date": "2024-06-25",
            "total_amount": 6600.00,
        },
        {
            "sale_id": 16,
            "employee_id": 12,
            "customer_id": 85,
            "region_id": 10,
            "sale_date": "2024-01-02",
            "total_amount": 5700.00,
        },
        {
            "sale_id": 17,
            "employee_id": 10,
            "customer_id": 76,
            "region_id": 6,
            "sale_date": "2025-01-07",
            "total_amount": 1400.00,
        },
        {
            "sale_id": 18,
            "employee_id": 2,
            "customer_id": 32,
            "region_id": 7,
            "sale_date": "2024-05-21",
            "total_amount": 1800.00,
        },
        {
            "sale_id": 19,
            "employee_id": 8,
            "customer_id": 93,
            "region_id": 2,
            "sale_date": "2025-02-04",
            "total_amount": 700.00,
        },
        {
            "sale_id": 20,
            "employee_id": 1,
            "customer_id": 64,
            "region_id": 1,
            "sale_date": "2024-09-11",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 21,
            "employee_id": 10,
            "customer_id": 50,
            "region_id": 6,
            "sale_date": "2024-06-01",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 22,
            "employee_id": 3,
            "customer_id": 100,
            "region_id": 9,
            "sale_date": "2024-06-02",
            "total_amount": 900.00,
        },
        {
            "sale_id": 23,
            "employee_id": 19,
            "customer_id": 39,
            "region_id": 9,
            "sale_date": "2024-06-07",
            "total_amount": 4400.00,
        },
        {
            "sale_id": 24,
            "employee_id": 14,
            "customer_id": 66,
            "region_id": 3,
            "sale_date": "2024-04-06",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 25,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-09-03",
            "total_amount": 4300.00,
        },
    ]
    return jsonify(sales)


@app.route('/employees/sales-summary', methods=['GET'])
def get_employee_sales_summary():
    employees = [
        {"employee_id": 1, "employee_name": "Alice Johnson", "region_id": 1},
        {"employee_id": 2, "employee_name": "Bob Smith", "region_id": 7},
        {"employee_id": 3, "employee_name": "Charlie Davis", "region_id": 9},
        {"employee_id": 4, "employee_name": "Diana Martinez", "region_id": 4},
        {"employee_id": 5, "employee_name": "Ethan Brown", "region_id": 6},
        {"employee_id": 6, "employee_name": "Fiona Wilson", "region_id": 7},
        {"employee_id": 7, "employee_name": "George Anderson", "region_id": 5},
        {"employee_id": 8, "employee_name": "Hannah Thompson", "region_id": 2},
        {"employee_id": 9, "employee_name": "Ian Clark", "region_id": 3},
        {"employee_id": 10, "employee_name": "Julia Rodriguez", "region_id": 6},
        {"employee_id": 11, "employee_name": "Kevin Lewis", "region_id": 4},
        {"employee_id": 12, "employee_name": "Laura Walker", "region_id": 10},
        {"employee_id": 13, "employee_name": "Michael Hall", "region_id": 1},
        {"employee_id": 14, "employee_name": "Natalie Young", "region_id": 3},
        {"employee_id": 15, "employee_name": "Oliver King", "region_id": 8
        },
        {"employee_id": 16, "employee_name": "Priya Patel", "region_id": 7},
        {"employee_id": 17, "employee_name": "Rahul Gupta", "region_id": 5},
        {"employee_id": 18, "employee_name": "Sara Lee", "region_id": 7},
        {"employee_id": 19, "employee_name": "Thomas Baker", "region_id": 9},
        {"employee_id": 20, "employee_name": "Uma Sharma", "region_id": 1},
    ]

    sales = [
        {
            "sale_id": 1,
            "employee_id": 6,
            "customer_id": 29,
            "region_id": 7,
            "sale_date": "2025-01-14",
            "total_amount": 400.00,
        },
        {
            "sale_id": 2,
            "employee_id": 4,
            "customer_id": 92,
            "region_id": 4,
            "sale_date": "2024-01-30",
            "total_amount": 4200.00,
        },
        {
            "sale_id": 3,
            "employee_id": 2,
            "customer_id": 43,
            "region_id": 7,
            "sale_date": "2024-06-05",
            "total_amount": 3100.00,
        },
        {
            "sale_id": 4,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-08-24",
            "total_amount": 800.00,
        },
        {
            "sale_id": 5,
            "employee_id": 16,
            "customer_id": 94,
            "region_id": 7,
            "sale_date": "2024-08-26",
            "total_amount": 5900.00,
        },
        {
            "sale_id": 6,
            "employee_id": 17,
            "customer_id": 73,
            "region_id": 5,
            "sale_date": "2024-01-30",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 7,
            "employee_id": 16,
            "customer_id": 37,
            "region_id": 7,
            "sale_date": "2024-12-17",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 8,
            "employee_id": 5,
            "customer_id": 47,
            "region_id": 6,
            "sale_date": "2024-04-22",
            "total_amount": 5500.00,
        },
        {
            "sale_id": 9,
            "employee_id": 4,
            "customer_id": 18,
            "region_id": 4,
            "sale_date": "2024-02-16",
            "total_amount": 2700.00,
        },
        {
            "sale_id": 10,
            "employee_id": 11,
            "customer_id": 17,
            "region_id": 4,
            "sale_date": "2024-12-09",
            "total_amount": 2900.00,
        },
        {
            "sale_id": 11,
            "employee_id": 13,
            "customer_id": 83,
            "region_id": 1,
            "sale_date": "2024-01-02",
            "total_amount": 8300.00,
        },
        {
            "sale_id": 12,
            "employee_id": 5,
            "customer_id": 54,
            "region_id": 6,
            "sale_date": "2024-06-02",
            "total_amount": 200.00,
        },
        {
            "sale_id": 13,
            "employee_id": 10,
            "customer_id": 23,
            "region_id": 6,
            "sale_date": "2024-02-17",
            "total_amount": 2400.00,
        },
        {
            "sale_id": 14,
            "employee_id": 12,
            "customer_id": 80,
            "region_id": 10,
            "sale_date": "2024-07-24",
            "total_amount": 1000.00,
        },
        {
            "sale_id": 15,
            "employee_id": 5,
            "customer_id": 59,
            "region_id": 6,
            "sale_date": "2024-06-25",
            "total_amount": 6600.00,
        },
        {
            "sale_id": 16,
            "employee_id": 12,
            "customer_id": 85,
            "region_id": 10,
            "sale_date": "2024-01-02",
            "total_amount": 5700.00,
        },
        {
            "sale_id": 17,
            "employee_id": 10,
            "customer_id": 76,
            "region_id": 6,
            "sale_date": "2025-01-07",
            "total_amount": 1400.00,
        },
        {
            "sale_id": 18,
            "employee_id": 2,
            "customer_id": 32,
            "region_id": 7,
            "sale_date": "2024-05-21",
            "total_amount": 1800.00,
        },
        {
            "sale_id": 19,
            "employee_id": 8,
            "customer_id": 93,
            "region_id": 2,
            "sale_date": "2025-02-04",
            "total_amount": 700.00,
        },
        {
            "sale_id": 20,
            "employee_id": 1,
            "customer_id": 64,
            "region_id": 1,
            "sale_date": "2024-09-11",
            "total_amount": 3400.00,
        },
        {
            "sale_id": 21,
            "employee_id": 10,
            "customer_id": 50,
            "region_id": 6,
            "sale_date": "2024-06-01",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 22,
            "employee_id": 3,
            "customer_id": 100,
            "region_id": 9,
            "sale_date": "2024-06-02",
            "total_amount": 900.00,
        },
        {
            "sale_id": 23,
            "employee_id": 19,
            "customer_id": 39,
            "region_id": 9,
            "sale_date": "2024-06-07",
            "total_amount": 4400.00,
        },
        {
            "sale_id": 24,
            "employee_id": 14,
            "customer_id": 66,
            "region_id": 3,
            "sale_date": "2024-04-06",
            "total_amount": 3500.00,
        },
        {
            "sale_id": 25,
            "employee_id": 3,
            "customer_id": 91,
            "region_id": 9,
            "sale_date": "2024-09-03",
            "total_amount": 4300.00,
        },
    ]

    summary_by_employee = {}

    for emp in employees:
        emp_id = emp["employee_id"]
        summary_by_employee[emp_id] = {
            "employee_id": emp_id,
            "employee_name": emp["employee_name"],
            "region_id": emp["region_id"],
            "total_sales": 0.0,
            "deals_closed": 0,
        }

    for sale in sales:
        emp_id = sale["employee_id"]
        if emp_id in summary_by_employee:
            summary_by_employee[emp_id]["total_sales"] += sale["total_amount"]
            summary_by_employee[emp_id]["deals_closed"] += 1

    return jsonify(list(summary_by_employee.values()))

if __name__ == '__main__':
    app.run(debug=True, port=10000)

