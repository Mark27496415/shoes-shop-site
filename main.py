from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kategorii/')
def kategorii():
    return render_template('kategorii.html')

@app.route('/kupit/')
def kupit():
    return render_template('kupit.html')

@app.route('/krosovki/')
def krosovki():
    return render_template('krosovki.html')

@app.route('/jentuf/')
def jentuf():
    return render_template('jentuf.html')

@app.route('/mujtuf/')
def mujtuf():
    return render_template('mujtuf.html')

@app.route('/mokas/')
def mokas():
    return render_template('mokas.html')

@app.route('/shlepki/')
def shlepki():
    return render_template('shlepki.html')

@app.route('/sabo/')
def sabo():
    return render_template('sabo.html')

if __name__ =='__main__':
    app.run()

