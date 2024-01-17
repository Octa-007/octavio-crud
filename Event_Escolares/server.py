
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect

from database import Database
from database import engine
from database import db_session
from flask import url_for

import models

app = Flask(__name__)
    
Database.metadata.create_all(engine)

@app.get('/')   #metodo get y su acceso en la raiz es decir como vamos a acceder desde el navegador
def home():   #definimos una funcion 
    evento = db_session.query(models.eventos).all()
    return render_template("home.html", lista_eventos=evento)


@app.post('/insertar')
def insertar():
    name = request.form['nombre']
    fecha = request.form['fecha']
    lugar = request.form['lugar']
    
    nuevo_evento = models.eventos(
        nombre = name,
        fecha = fecha,
        lugar = lugar,
    )
    db_session.add(nuevo_evento)
    db_session.commit()
    return redirect("/")

@app.get('/eliminar/<id>')
def eliminar(id):
   evento = db_session.query(models.eventos).get(id)
   
   if evento == None:
       flash('ID no encontrado')
       return render_template('home.html')
   
   db_session.delete(evento)
   db_session.commit()
   
   return redirect(url_for('home'))  
   
@app.post('/actualizar/<id>')
def actualizar(id):
    evento = db_session.query(models.eventos).get(id)
       
    if evento == None:
        flash('ID no encontrado')
        return redirect (url_for('home'))
       
    nomb = request.form['name_act']
    fech = request.form['fecha_act']
    lugar = request.form['lugar_act']
       
    if evento == None:
        flash('No hay nada')
        return redirect (url_for('home'))
       
    evento.nombre = nomb
    evento.fecha=fech
    evento.lugar = lugar
       
    db_session.add(evento)
    db_session.commit()
       
    return redirect(url_for('home'))
   
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 7070, debug=True)
    
    