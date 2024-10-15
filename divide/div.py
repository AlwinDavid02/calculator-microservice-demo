from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

