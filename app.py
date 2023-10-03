import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained classifier from the pickle file
with open('iris_classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Load the Iris dataset for species names
iris_target_names = ["setosa", "versicolor", "virginica"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Make a prediction using the classifier
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = classifier.predict(input_data)[0]

        # Map the prediction to the corresponding Iris species
        species = iris_target_names[prediction]

        return render_template('index.html', prediction=f'The predicted Iris species is {species}')
    return render_template('index.html', prediction='')

if __name__ == '__main__':
    app.run(debug=True)
