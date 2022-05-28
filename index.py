from flask import Flask, render_template

app = Flask(__name__)

#Crear la ruta principal
@app.route('/')
def home():
    return render_template('home.html')

#Crea una ruta alternativa
@app.route('/about')
def aboyt():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)