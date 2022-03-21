############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)

# Parcial
# Mysql Connection
#! profesor nos vimos en la 
#! necesidad de cambiar el puerto
#! de xampp para que no se bloquera 
#! con el puerto de workbench 
#! el puerto es :
#? PORT:3307 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyect_uni'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"


#!------------------------------usuario------------------------------
@app.route('/getAll', methods=['GET'])
def getAll():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_usuario': result[0], 'Tipo_doc': result[1],
                       'Num_doc': result[2], 'Nombre': result[3],
                       'Apellido': result[4], 'Id_rol': result[5],
                       'Estado': result[6], 'Fecha': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllById/<id>', methods=['GET'])
def getAllById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE Id_usuario = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_usuario': result[0], 'Tipo_doc': result[1],
                       'Num_doc': result[2], 'Nombre': result[3],
                       'Apellido': result[4], 'Id_rol': result[5],
                       'Estado': result[6], 'Fecha': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


#### ruta para crear un registro########


@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    try:
        if request.method == 'POST':
            Id_usuario = request.json['Id_usuario']  # nombre
            Tipo_doc = request.json['Tipo_doc']  # telefono
            Num_doc = request.json['Num_doc']  # email
            Nombre = request.json['Nombre']
            Apellido = request.json['Apellido']
            Id_rol = request.json['Id_rol']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO usuario (Id_usuario, Tipo_doc, Num_doc , Nombre , Apellido , Id_rol, Estado , Fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (Id_usuario, Tipo_doc, Num_doc, Nombre, Apellido, Id_rol, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})

    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


######### ruta para actualizar################
@app.route('/update_usuario/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        Id_usuario = request.json['Id_usuario']  # nombre
        Tipo_doc = request.json['Tipo_doc']  # telefono
        Num_doc = request.json['Num_doc']  # email
        Nombre = request.json['Nombre']
        Apellido = request.json['Apellido']
        Id_rol = request.json['Id_rol']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE usuario SET Id_usuario = %s , Tipo_doc = %s , Num_doc = %s , Nombre = %s , Apellido= %s , Id_rol = %s ,Estado =%s , Fecha = %s WHERE Id_usuario = %s; """,
                    (Id_usuario, Tipo_doc, Num_doc, Nombre, Apellido, Id_rol, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_usuario/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM usuario WHERE Id_usuario = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})
#! --------------------------roles -----------------------------------


@app.route('/add_rol', methods=['POST'])
def add_rol():
    try:
        if request.method == 'POST':
            Id_rol = request.json['Id_rol']
            Nombre = request.json['Nombre']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO rol (Id_rol, Nombre, Estado, Fecha) VALUES (%s, %s, %s, %s)",
                        (Id_rol, Nombre, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})

    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

#! ---------------------------materia------------------------------


@app.route('/getAllByMa/<id>', methods=['GET'])
def getAllByMa(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM materia WHERE Id_materia = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_materia': result[0], 'Nombre': result[1],
                       'Estado': result[2], 'Fecha': result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)

        return jsonify({"informacion": e})


@app.route('/getAllMa', methods={'GET'})
def getAllMa():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM materia ')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_materia': result[0], 'Nombre': result[1],
                       'Estado': result[2], 'Fecha': result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)

        return jsonify({"informacion": e})


@app.route('/add_materia', methods=['POST'])
def add_materia():
    try:
        if request.method == 'POST':
            Id_materia = request.json['Id_materia']
            Nombre = request.json['Nombre']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO materia (Id_materia, Nombre, Estado, Fecha) VALUES (%s, %s, %s, %s)",
                        (Id_materia, Nombre, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/update_materia/<id>', methods=['PUT'])
def update_materia(id):

    try:
        Id_materia = request.json['Id_materia']
        Nombre = request.json['Nombre']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE materia SET Id_materia = %s , Nombre = %s , Estado =%s , Fecha = %s WHERE Id_materia = %s; """,
                    (Id_materia,  Nombre, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_materia/<id>', methods=['DELETE'])
def delete_materia(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM materia WHERE Id_materia = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


#!--------------------------estudiante--------------------------------

@app.route('/getAllEs/', methods=['GET'])
def getAllEs():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM estudiante')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_estudiante': result[0], 'Id_usuario': result[1],
                       'Semestre': result[2],
                       'Estado': result[3], 'Fecha': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllByEs/<id>', methods=['GET'])
def getAllByEs(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM estudiante WHERE Id_estudiante = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_estudiante': result[0], 'Id_usuario': result[1],
                       'Semestre': result[2],
                       'Estado': result[3], 'Fecha': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/add_estudiante', methods=['POST'])
def add_estudiante():
    try:
        if request.method == 'POST':
            Id_estudiante = request.json['Id_estudiante']
            Id_usuario = request.json['Id_usuario']
            Semestre = request.json['Semestre']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO estudiante (Id_estudiante,Id_usuario, Semestre, Estado, Fecha) VALUES (%s, %s, %s, %s, %s)",
                        (Id_estudiante, Id_usuario, Semestre, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/update_estudiante/<id>', methods=['PUT'])
def update_estudiante(id):
    try:
        Id_estudiante = request.json['Id_estudiante']
        Id_usuario = request.json['Id_usuario']
        Semestre = request.json['Semestre']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE estudiante SET Id_estudiante = %s , Id_usuario = %s,Semestre = %s , Estado =%s , Fecha = %s WHERE Id_estudiante = %s; """,
                    (Id_estudiante, Id_usuario, Semestre, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_estudiante/<id>', methods=['DELETE'])
def delete_estudiante(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM estudiante WHERE Id_estudiante = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


#!-----------------------------profesor--------------------------------

@app.route('/getAllPo', methods=['GET'])
def getAllPo():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM profesor')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_profesor': result[0], 'Id_usuario': result[1],
                       'Facultad': result[2],
                       'Estado': result[3], 'Fecha': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllByPo/<id>', methods=['GET'])
def getAllByPo(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM profesor WHERE Id_profesor = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_profesor': result[0], 'Id_usuario': result[1],
                       'Facultad': result[2],
                       'Estado': result[3], 'Fecha': result[4]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/add_profesor', methods=['POST'])
def add_profesor():
    try:
        if request.method == 'POST':
            Id_profesor = request.json['Id_profesor']
            Id_usuario = request.json['Id_usuario']
            Facultad = request.json['Facultad']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO profesor (Id_profesor,Id_usuario, Facultad, Estado, Fecha) VALUES (%s, %s, %s, %s, %s)",
                        (Id_profesor, Id_usuario, Facultad, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/update_profesor/<id>', methods=['PUT'])
def update_profesor(id):
    try:
        Id_profesor = request.json['Id_profesor']
        Id_usuario = request.json['Id_usuario']
        Facultad = request.json['Facultad']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE profesor SET Id_profesor = %s , Id_usuario = %s,Facultad = %s , Estado =%s , Fecha = %s WHERE Id_profesor = %s; """,
                    (Id_profesor, Id_usuario, Facultad, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_profesor/<id>', methods=['DELETE'])
def delete_profesor(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM profesor WHERE Id_profesor = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})
# fvneovnerpovnerpovnerpvoenrmvpo

#!---------------------------------grupo--------------------------------------
@app.route('/getAllGru', methods=['GET'])
def getAllGru():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM grupo')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_grupo': result[0], 'Estado': result[1], 'Fecha': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/getAllByGru/<id>', methods=['GET'])
def getAllByGru(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM grupo WHERE Id_grupo = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_grupo': result[0],'Estado': result[1], 'Fecha': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/add_grupo', methods=['POST'])
def add_grupo():
    try:
        if request.method == 'POST':
            Id_grupo = request.json['Id_grupo']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO grupo (Id_grupo , Estado, Fecha) VALUES (%s, %s, %s)",
                        (Id_grupo, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/update_grupo/<id>',methods=['PUT'])
def update_grupo(id):
    try:
        Id_grupo = request.json['Id_grupo']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE grupo SET Id_grupo = %s , Estado =%s , Fecha = %s WHERE Id_grupo = %s; """,
                    (Id_grupo, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/delete_grupo/<id>', methods=['DELETE'])
def delete_grupo(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM grupo WHERE Id_grupo = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})
#!-------------------------grupo_estu-------------------------


@app.route('/getAllGs', methods=['GET'])
def getAllGs():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM grupo_estu ',)
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_grupo_estu': result[0],'Id_grupo': result[1], 'Id_estudiante': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/getAllByGs/<id>', methods=['GET'])
def getAllByGs(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM grupo_estu WHERE Id_grupo = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_grupo_estu': result[0],'Id_grupo': result[1], 'Id_estudiante': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})



@app.route("/add_gs", methods=['POST'])
def add_gs():
    try:
        if request.method == 'POST':
            Id_grupo_estu = request.json['Id_grupo_estu']
            Id_grupo = request.json['Id_grupo']
            Id_estudiante = request.json['Id_estudiante']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO grupo_estu (Id_grupo_estu , Id_grupo, Id_estudiante) VALUES (%s, %s, %s)",
                        (Id_grupo_estu, Id_grupo, Id_estudiante))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/update_gs/<id>',methods=['PUT'])
def update_gs(id):
    try:
        Id_grupo_estu = request.json['Id_grupo_estu']
        Id_grupo = request.json['Id_grupo']
        Id_estudiante = request.json['Id_estudiante']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE grupo_estu SET Id_grupo_estu = %s , Id_grupo =%s , Id_estudiante = %s WHERE Id_grupo_estu = %s; """,
                    (Id_grupo_estu ,Id_grupo, Id_estudiante, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/delete_gs/<id>', methods=['DELETE'])
def delete_gs(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM grupo_estu WHERE Id_grupo_estu = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

#!--------------------------proyecto----------------------
@app.route('/getAllPy', methods=['GET'])
def getAllPy():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM proyecto')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_proyecto': result[0],'Id_grupo': result[1],'Id_materia': result[2], 'Nombre' : result[3], 'Estado': result[4], 'Fecha': result[5]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/getAllByPy/<id>', methods=['GET'])
def getAllByPy(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM proyecto WHERE Id_proyecto = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_proyecto': result[0], 'Id_grupo': result[1],'Id_materia': result[2],
                       'Nombre': result[3],
                       'Estado': result[4], 'Fecha': result[5]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})



@app.route('/add_py', methods=['POST'])
def add_py():
    try:
        if request.method == 'POST':
            Id_proyecto = request.json['Id_proyecto']
            Id_grupo = request.json['Id_grupo']
            Id_materia = request.json['Id_materia']
            Nombre = request.json['Nombre']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO proyecto (Id_proyecto , Id_grupo, Id_materia,Nombre, Estado, Fecha) VALUES (%s, %s, %s,%s, %s, %s)",
                        (Id_proyecto, Id_grupo, Id_materia, Nombre, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/update_py/<id>',methods=['PUT'])
def update_py(id):
    try:
        Id_proyecto = request.json['Id_proyecto']
        Id_grupo = request.json['Id_grupo']
        Id_materia = request.json['Id_materia']
        Nombre = request.json['Nombre']
        Estado = request.json['Estado']
        Fecha = request.json['Fecha']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE proyecto SET Id_proyecto = %s , Id_grupo =%s , Id_materia = %s, Nombre=%s , Estado=%s, Fecha=%s  WHERE Id_proyecto = %s; """,
                    (Id_proyecto, Id_grupo, Id_materia, Nombre, Estado, Fecha, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_py/<id>', methods=['DELETE'])
def delete_py(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM proyecto WHERE Id_proyecto = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})
#!----------------------nota----------------------

@app.route('/getAllNo', methods=['GET'])
def getAllNo():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM nota')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_nota': result[0],'Id_proyecto': result[1], 'Nota': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/getAllByNo/<id>', methods=['GET'])
def getAllByNo(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM nota WHERE Id_nota = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_nota': result[0],'Id_proyecto': result[1], 'Nota': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/add_nota', methods=['POST'])
def add_nota():
    try:
        if request.method == 'POST':
            Id_nota = request.json['Id_nota']
            Id_proyecto = request.json['Id_proyecto']
            Nota = request.json['Nota']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO nota (Id_nota, Id_proyecto, Nota) VALUES (%s, %s, %s)",
                        (Id_nota ,Id_proyecto, Nota))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

@app.route('/update_no/<id>',methods=['PUT'])
def update_no(id):
    try:
        Id_nota = request.json['Id_nota']
        Id_proyecto = request.json['Id_proyecto']
        Nota = request.json['Nota']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE nota SET Id_nota = %s , Id_proyecto =%s , Nota = %s WHERE Id_nota = %s; """,
                    (Id_nota ,Id_proyecto, Nota, id))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


@app.route('/delete_no/<id>', methods=['DELETE'])
def delete_no(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM nota WHERE Id_nota = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion": "Registro eliminado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})

#! starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
