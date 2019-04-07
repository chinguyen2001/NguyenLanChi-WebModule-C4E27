from flask import Flask, render_template
app = Flask(__name__)


@app.route('/aboutme')
def aboutme():
    app_me = {
        "Name" : "Nguyễn Lan Chi",
        "Age" : "18",
        "Hobbies" : "Game",      
        "Gender" : "Female"
    }
    return render_template("aboutme.html",
                            about_me = app_me)


if __name__ == '__main__':
  app.run(debug=True)