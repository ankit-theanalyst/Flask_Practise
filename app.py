#our obective to write this code is to perform simple addition, substraction, multiplication etc using html form

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


#creating the home page

@app.route('/', methods = ["GET","POST"])
def home_page():
    return render_template("index.html")


#creating a function for the operation
#for this function to be called when the submit button is clicked, we need to set the route according to the set action in the index.html
@app.route("/math",methods = ["POST"])
def math_operation1():
    #checking the type of method
    if(request.method == "POST"):
        #pulling the data from the html form
        operation_requested = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        
        #calculating the result according to the requested operation
        if(operation_requested == 'add'):
            addition = num1 + num2
            result = "the result of addition of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(addition)
        if(operation_requested == 'subtract'):
            subtract = num1 - num2
            result = "the result of subtraction of " + str(num1) + " and "+  str(num2) +" is " + str(subtract)
        if(operation_requested == 'multiply'):
            multiply = num1 * num2
            result = "the result of multiplication of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(multiply)
        if(operation_requested == 'divide'):
            divide = num1/num2
            result = "the result of division of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(divide)

            #sending the result to the result.html file
        return render_template("results.html",result = result)


#using json source to fill the form
@app.route("/postman_data",methods = ["POST"])
def math_operation():
    #checking the type of method
    if(request.method == "POST"):
        #pulling the data from the html form
        operation_requested = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        
        #calculating the result according to the requested operation
        if(operation_requested == 'add'):
            addition = num1 + num2
            result = "the result of addition of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(addition)
        if(operation_requested == 'subtract'):
            subtract = num1 - num2
            result = "the result of subtraction of " + str(num1) + " and "+  str(num2) +" is " + str(subtract)
        if(operation_requested == 'multiply'):
            multiply = num1 * num2
            result = "the result of multiplication of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(multiply)
        if(operation_requested == 'divide'):
            divide = num1/num2
            result = "the result of division of" + " " + str(num1) + " " + "and" + " "+  str(num2) +" "+ "is" + " " + str(divide)

            #sending the result to the result.html file
        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
