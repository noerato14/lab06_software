from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario
 

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()
ruta='/usuario'

@app.route('/')
def inicio():
    return render_template('index.html')





@app.route('/register')
def register():
    data = db.read(None)
    print("data",data)
    return render_template('register.html', data = data)

@app.route('/register/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))

@app.route('/validation', methods = ['POST', 'GET'])

def validation():
    flagLogin = False
    data = db.read(None)

    if request.method == 'POST' and request.form['save']:
        for i in range (0,len(data)):
            if request.form.get('username') == data[i][3]:
                if request.form.get('clave')== data[i][4]:
                    flagLogin = True
                    userType = data[i][5]
                    break
                else:
                    flagLogin = False
            else:
                flagLogin = False
                
        if flagLogin == True:
            if userType == 'alumno':
                return redirect(url_for('alumno'))
        
            elif userType == 'profesor':
                return redirect(url_for('profesor'))
        else:
            return redirect(url_for('inicio'))

    else:
        return redirect(url_for('inicio'))

@app.route('/profesor')
def profesor():
    data = db.read(None)
    return render_template('profesor/index.html', data = data)

@app.route('/alumno')
def alumno():
    data = db.read(None)
    return render_template('alumno/index.html', data = data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
