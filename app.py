from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load models
with open('ridge.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        input_data = {
            'Temperature': float(request.form['Temperature']),
            'RH': float(request.form['RH']),
            'Ws': float(request.form['Ws']),
            'Rain': float(request.form['Rain']),
            'FFMC': float(request.form['FFMC']),
            'DMC': float(request.form['DMC']),
            'ISI': float(request.form['ISI']),
            'Classes': float(request.form['Classes']),
            'Region': float(request.form['Region'])
        }

        df = pd.DataFrame([input_data])
        scaled = scaler.transform(df)
        prediction = model.predict(scaled)

        return render_template('index.html', prediction=prediction[0])

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
