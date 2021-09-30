from flask import Flask, request
import random

app = Flask(__name__)

label_dic = {0 : "Setosa", 1 : "Versicolour", 2 : "Virginica"}
import pickle
model = pickle.load(open("model.sav", 'rb'))

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    """ Makes predictions using trained ML model """
    X = [[sepal_length, sepal_width, petal_length, petal_width]]
    predict_label = model.predict(X)[0]
    return label_dic[predict_label]

@app.route("/api/iris")
def index():
    sepal_length = request.args.get("sepal_length", "")
    sepal_width = request.args.get("sepal_width", "")
    petal_length = request.args.get("petal_length", "")
    petal_width = request.args.get("petal_width", "")
    if petal_length and petal_width and sepal_length and sepal_width:
        flower_species = predict_iris(float(sepal_length), float(sepal_width), 
                                      float(petal_length), float(petal_width))
    else:
        flower_species = ""
    return """<form action="" method="get"> \
                Sepal Length: <input type="text" name="sepal_length"> \
                Sepal Width: <input type="text" name="sepal_width"> \
                Petal Length: <input type="text" name="petal_length"> \
                Petal Width: <input type="text" name="petal_width"> \
                <input type="submit" value="Predict"> \
                Flower Species: {}
              </form>""".format(flower_species)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
