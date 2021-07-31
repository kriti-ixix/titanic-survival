#Importing the libraries
from flask import Flask, render_template, request
import pickle

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open("titanic.pkl", "rb"))

#User-defined functions
@app.route("/", methods=["GET"])
def Home():
    return render_template("titanic.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    pclass = int(request.form['pclass'])
    gender = request.form['gender']
    embarked = request.form['embarked']

    s = 0 
    q = 0

    if gender == 'M':
        gender = 1
    else:
        gender = 0

    if embarked == "S":
        s = 1
        q = 0
    elif embarked == "Q":
        s = 0
        q = 1
    else:
        s = 0
        q = 0

    prediction = loadedModel.predict([[pclass, age, sibsp, parch, fare, gender, q, s]])[0]
    
    if prediction == 0:
        prediction = "Did not survive"
    else:
        prediction = "Survived"

    return render_template("titanic.html", prediction_output=prediction)


#Main function
if __name__ == "__main__":
    app.run(debug=True)