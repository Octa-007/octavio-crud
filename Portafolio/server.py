
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect

from flask import url_for

app = Flask(__name__)

@app.get('/octavio')   #metodo get y su acceso en la raiz es decir como vamos a acceder desde el navegador
def home():   #definimos una funcion 
    return render_template("index.html")
   
if __name__ == '__main__':
    app.run('0.0.0.0', 7979, debug=True)
    
    