from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portifólio')
def port():
    return render_template('portifolio.html')

@app.route('/educação')
def edu():
    return render_template('educacao.html')

@app.route('/sobre-mim')
def sobre():
    return render_template('sobre-mim.html')

@app.route('/portifólio/1')
def pro1():
    return render_template('pro1.html')

@app.route('/portifólio/2')
def pro2():
    return render_template('pro2.html')

@app.route('/portifólio/3')
def pro3():
    return render_template('pro3.html')

@app.route('/portifólio/4')
def pro4():
    return render_template('pro4.html')

@app.route('/portifólio/5')
def pro5():
    return render_template('pro5.html')

@app.route('/educação/certificados')
def cert():
    return render_template('certificado.html')


app.run()