from flask import Flask, render_template
from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/school')
def school():
    return redirect("http://techkids.vn")


if __name__ == '__main__':
  app.run(debug=True)