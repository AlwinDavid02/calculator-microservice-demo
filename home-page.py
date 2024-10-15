from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URLs of the operation microservices
SERVICES = {
    'add': 'http://localhost:5001/add',
    'subtract': 'http://localhost:5002/subtract',
    'multiply': 'http://localhost:5003/multiply',
    'divide': 'http://localhost:5004/divide',
}

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')

        # Send request to the appropriate operation service
        response = requests.post(SERVICES[operation], json={'num1': num1, 'num2': num2})

        if response.ok:
            result = response.json().get('result')
        else:
            result = "Error communicating with the operation service."

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
