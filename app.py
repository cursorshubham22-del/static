from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    return "I am Palak!!!!"

@app.route('/sales/all')
def salesAll():
    return '{"month":"Sep","amount":1000000}'

if __name__ == '__main__':
    app.run(debug=True, port=10000)
