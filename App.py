############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# initializations
app = Flask(__name__)
CORS(app)


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyect_uni'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)

# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"


#! ruta para consultar todos los registros
@app.route('/getAll', methods=['GET'])
def getAll():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM estudiante')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'Id_estudiante': result[0], 'Tipo_doc': result[1],
                       'Num_doc': result[2], 'Nombre': result[3],
                       'Apellido': result[4], 'Curso': result[5],
                       'Estado': result[6], 'Fecha': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


# # ruta para consultar todos los registros
# @app.route('/getAll', methods=['GET'])
# def getAll():
#     try:
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM contacts')
#         rv = cur.fetchall()
#         cur.close()
#         payload = []
#         content = {}
#         for result in rv:
#             content = {'id': result[0], 'fullname': result[1],
#                        'phone': result[2], 'email': result[3]}
#             payload.append(content)
#             content = {}
#         return jsonify(payload)
#     except Exception as e:
#         print(e)
#         return jsonify({"informacion": e})

# ruta para consultar por parametro
@app.route('/getAllById/<id>', methods=['GET'])
def getAllById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'fullname': result[1],
                     'phone': result[2], 'email': result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


#### ruta para crear un registro########
@app.route('/add_estudiante', methods=['POST'])
def add_estudiante():
    try:
        if request.method == 'POST':
            Id_estudiante = request.json['Id_estudiante']  # nombre
            Tipo_doc = request.json['Tipo_doc']  # telefono
            Num_doc = request.json['Num_doc']  # email
            Nombre = request.json['Nombre']
            Apellido = request.json['Apellido']
            Curso = request.json['Curso']
            Estado = request.json['Estado']
            Fecha = request.json['Fecha']
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO estudiante (Id_estudiante, Tipo_doc, Num_doc , Nombre , Apellido , Curso , Estado , Fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                 (Id_estudiante, Tipo_doc, Num_doc, Nombre, Apellido, Curso, Estado, Fecha))
            mysql.connection.commit()
            return jsonify({"informacion": "Registro exitoso"})

    except Exception as e:
        print(e)
        return jsonify({"informacion": e})


######### ruta para actualizar################
@app.route('/update/<id>', methods=['PUT'])
def update_contact(id):
    try:
        fullname = request.json['fullname']
        phone = request.json['phone']
        email = request.json['email']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
        """, (fullname, email, phone, id))
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


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
