from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Load precomputed feature importances
    importances = pd.read_csv("data/feature_importances.csv")
    return render_template("index.html", tables=[importances.to_html(classes='data', header="true")])

if __name__ == "__main__":
    app.run(debug=True)
