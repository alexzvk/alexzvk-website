from flask import Flask, render_template, send_file
import pathlib
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/resume')
def show_resume():
    return send_file('Alex Van Kuiken Resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)