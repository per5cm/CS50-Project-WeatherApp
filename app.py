from flask import Flask, render_template, request
from project import main as get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    city = ""
    state = ""
    country = "Germany"
    
    if request.method == "POST":  
        city = request.form.get("cityName").strip()
        state = request.form.get("stateName").strip()
        country = request.form.get("countryName").strip()
        data = get_weather(city, state, country)
    return render_template("index.html", data=data, city=city, state=state, country=country)

if __name__ == "__main__":
    app.run(debug=True)