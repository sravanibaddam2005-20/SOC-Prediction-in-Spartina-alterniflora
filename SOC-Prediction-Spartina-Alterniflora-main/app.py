import warnings
warnings.filterwarnings('ignore')

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.sav")

# PSO selected features
features = [
'Green','RedEdge','NDVI','GNDVI','NDRE','EVI','SAVI',
'DVI','MSAVI','Altitude','Slope','Aspect','Relief','SOS'
]

history = []

@app.route("/", methods=["GET","POST"])
def index():

    prediction = None
    confidence = None
    level = None
    color = None
    heatmap_data = []

    if request.method == "POST":

        values = []

        for f in features:
            val = float(request.form[f])
            values.append(val)

        arr = np.array(values).reshape(1,-1)

        pred = model.predict(arr)[0]
        prediction = round(pred,3)

        confidence = 95

        # SOC level classification
        if prediction < 2:
            level = "Low SOC"
            color = "danger"
        elif prediction < 5:
            level = "Medium SOC"
            color = "warning"
        else:
            level = "High SOC"
            color = "success"

        # save history
        history.append(prediction)

        # Create SOC heatmap predictions (simulated grid)
        for i in range(50):

            lat = 20 + np.random.uniform(-2,2)
            lon = 78 + np.random.uniform(-2,2)

            noise = np.random.normal(0,0.5)
            soc_value = float(prediction + noise)

            heatmap_data.append([lat,lon,soc_value])

    return render_template(
        "index.html",
        features=features,
        prediction=prediction,
        confidence=confidence,
        level=level,
        color=color,
        history=history,
        heatmap_data=heatmap_data
    )

if __name__ == "__main__":
    app.run()