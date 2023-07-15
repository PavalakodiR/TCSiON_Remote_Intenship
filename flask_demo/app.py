import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = pickle.load(open('hr.pkl', 'rb'))

@app.route('/')
def entry():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/index')  # Modified route decorator
def index():
    return render_template('index.html')




@app.route('/getdata', methods=['POST'])
def submit():
    Role = request.form['Role']
    experience = request.form['Years of Experience']

    # Convert Role to numeric value using LabelEncoder
    label_encoder = LabelEncoder()
    role_encoded = label_encoder.fit_transform([Role])[0]

    variables = [[role_encoded, int(experience)]]

    result = model.predict(variables)
    salary_prediction = int(result)

    return render_template('result.html', salary=salary_prediction)


if __name__ == "__main__":
    app.run(debug=True)

