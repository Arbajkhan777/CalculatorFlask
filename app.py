from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask."

@app.route('/cal', methods=['GET'])
def math_operation():
    operation =     
    number1 = 
    number2 = 

    if operation == "addition":
        result = number1+number2
    elif operation == "multiplication":
        result = number1*number2
    elif operation == "division":
        result = number1/number2
    else:
        result = number1-number2
    return result



if __name__=='__main__':
    app.run()
