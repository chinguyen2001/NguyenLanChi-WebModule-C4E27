from flask import *
from BikeData import Bike_Services
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('BikeRental.html')

@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template('BikeRental.html')
    elif request.method == "POST":
        form = request.form 
        model = form["input_model"]
        dailyfee = form["input_dailyfee"]
        image = form["input_image"]
        year = form["input_year"]
        print(form)
        bikes = {
            "model" : model,
            "dailyfee" : dailyfee,
            "image" : image,
            "year" : year,
        }
        Bike_Services.insert_one(bikes)
        return redirect('/new_bike')

if __name__ == '__main__':
  app.run(debug=True)