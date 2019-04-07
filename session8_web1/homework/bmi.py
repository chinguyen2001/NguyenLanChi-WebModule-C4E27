from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height = height/100
    BMI = weight/(height**2)
    return render_template('BMI.html',BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)