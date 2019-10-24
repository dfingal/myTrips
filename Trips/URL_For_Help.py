from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('home.html')

@app.route('/beaches/<name>')

def penguine_name(name):
    return render_template('beaches.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)