from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    result = num1 - num2
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
