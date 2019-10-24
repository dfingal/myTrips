from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('home.html')

@app.route('/trips/<name>')

def penguine_name(name):

    if(name == 'dubai'):
        text = 'Dubai is a really cool city.'
    elif(name == 'italy'):
        text = 'Italy is a really old city with lots of ruins.'
    elif(name == 'london'):
        text ="London is a mixture of old and new."
    elif(name == 'france'):
        text ='South of France has lots of cool architecture and good restaurants.'
    elif(name =='tulum'):
        text ='Tulum is filled with acient Mayan ruins and lots of beautiful beaches.'
    else:
        return 'Whoops! Not sure what you\'re talking about'

    return render_template('trips.html', name=name, text = text, image = name+'.jpg')



if __name__ == '__main__':
    app.run(debug=True)