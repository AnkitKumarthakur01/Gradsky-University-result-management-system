from flask import Flask, render_template
import pandas as pd

app = Flask(_name_)

@app.route("/")
def home():
    df = pd.read_csv("output/processed_results.csv")
    return render_template("index.html", tables=[df.to_html()], titles=df.columns.values)

if _name_ == "_main_":
    app.run(debug=True)