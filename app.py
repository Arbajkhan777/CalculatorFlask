from flask import Flask, request, render_template,jsonify
import json


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask."

@app.route('/cal', methods=['GET'])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number1"]

    if operation == "addition":
        result = int(number1)+int(number2)
    elif operation == "multiplication":
        result = int(number1)*int(number2)
    elif operation == "division":
        result = int(number1)/int(number2)
    else:
        result = int(number1)-int(number2)
    return "The operation is {} and the result is {}".format(operation, result)



if __name__=='__main__':
    app.run()
