from flask import Flask, request, render_template
import pickle
import numpy as np
from param import output

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values (as dict)
        form_data = request.form.to_dict()

        # Convert to float list
        features = [float(x) for x in form_data.values()]

        # Unpack
        GrLivArea, OverallQual, GarageCars, GarageArea, TotalBsmtSF, FirstFlrSF, FullBath = features

        errors = []

        # -------- VALIDATIONS -------- #

        if GrLivArea < 300:
            errors.append("❌ Living Area must be greater than 300 sq ft")

        if not (1 <= OverallQual <= 10):
            errors.append("❌ Overall Quality must be between 1 and 10")

        if GarageCars < 0:
            errors.append("❌ Garage Cars cannot be negative")

        if GarageArea < 0:
            errors.append("❌ Garage Area cannot be negative")

        if TotalBsmtSF < 0:
            errors.append("❌ Basement Area cannot be negative")

        if FirstFlrSF < 0:
            errors.append("❌ 1st Floor Area cannot be negative")

        if FullBath < 0 or FullBath > 5:
            errors.append("❌ Bathrooms must be between 0 and 5")

        # If errors exist → show them
        if errors:
            return render_template(
                'index.html',
                prediction_text="<br>".join(errors),
                form_data=form_data
            )

        # -------- PREDICTION -------- #

        final_features = np.array([features])
        prediction = model.predict(final_features)

        output = int(prediction[0])

        formatted_price = "₹{:,.0f}".format(output)

        if output < 100000:
            category = "Low Price"
        elif output < 200000:
            category = "Medium Price"
        else:
            category = "High Price"

        return render_template(
            'index.html',
            prediction_text=f"Predicted Price: {formatted_price} ({category})",
            form_data=form_data
        )

    except:
        return render_template(
            'index.html',
            prediction_text="❌ Invalid input. Please enter valid numbers.",
            form_data=request.form
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
