from flask import Flask, render_template, request, jsonify, url_for
import math


app = Flask(__name__)


@app.route("/",  methods=['GET','POST'])
def home():
    try:
        if request.method == "POST":
            operand = request.form['operand']
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            if operand == "+":
                result = num1 + num2
            elif operand == "-":
                result = num1 - num2
            elif operand == "/":
                result = num1 / num2
            elif operand == "*":
                result = num1 * num2
            elif operand == "**":
                result = num1 ** num2
            elif operand == "sqrt":
                new = num1 + num2
                result = math.sqrt(new)
            else:
                result = "That is not a valid operand. Please try again"
        else:
            result = "Hello, please feel free to use this calculator"
    except ValueError:
        result = f"No letters are allowed. Please try again"
    except ZeroDivisionError:
        result = f"Can't divide into zero. Please try again"

    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)