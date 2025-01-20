from flask import Flask , request , Response , jsonify

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return "This is calculator app"

@app.route('/calculator',methods = ['GET','POST'])
def calculator():
    data = request.get_json()
    print(data)
    operation = data.get('operation')
    num1 = int(data.get("num1"))
    num2 = int(data.get('num2'))

    if operation == 'add':
        return str(num1+num2)
    elif operation == 'subtract':
        return str(num1-num2)
    elif operation == 'multiply':
        return str(num1*num2)
    elif operation =='divide':
        return str(num1/num2)
    else:
        return "Invalid operation \n Please try again"

@app.route('/calculator_browser',methods = ['GET','POST'])
def calculator_browser():
    operation = request.args.get('operation')
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get('num2'))

    if operation == 'add':
        return str(num1+num2)
    elif operation == 'subtract':
        return str(num1-num2)
    elif operation == 'multiply':
        return str(num1*num2)
    elif operation =='divide':
        return str(num1/num2)
    else:
        return "Invalid operation \n Please try again"

if __name__=="__main__":
    app.run(debug=True)