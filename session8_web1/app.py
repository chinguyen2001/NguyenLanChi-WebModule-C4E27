from flask import Flask, render_template
app = Flask(__name__)


@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return str(a + b)

@app.route('/poem')
def poem():
    # poem_title = "Everything I Need"
    # poem_content = "Born on the wrong side of the ocean"
    # poem_author = "Lan Chi"
    app_poem = [{
        "title" : "Everything I need",
        "content" : "Born on the wrong side of the ocean",
        "author" : "Itachi",      
        "gender" : "male"
    },
    {
        "title" : "Thơ con cóc",
        "content" : "Đêm nay trăng lên cao quá",
        "author" : "Lan Chi",
        "gender" : "female"
    },
    ]

    return render_template("poem.html", 
                            poems = app_poem)


if __name__ == '__main__':
  app.run(debug=True)
 