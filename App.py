############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)

# Parcial
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyect_uni'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"


# * --------usuario-------
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
        cur.execute(""" UPDATE usuario SET Id_usuario = %s , Tipo_doc = %s , Num_doc = %s , Nombre = %s , Apellido= %s , Id_rol = %s ,Estado =%s , Fecha = %s WHERE Id_usuario = %s; """ , (Id_usuario, Tipo_doc, Num_doc, Nombre, Apellido, Id_rol, Estado, Fecha, id))
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
#* --------roles --------


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









#! starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
