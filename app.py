from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']
    result = None
    if operation == '+': result = calc.add(num1, num2)
    elif operation == '-': result = calc.subtract(num1, num2)
    elif operation == '*': result = calc.multiply(num1, num2)
    elif operation == '/': result = calc.divide(num1, num2)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
