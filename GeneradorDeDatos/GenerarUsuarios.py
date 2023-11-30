from DBConnect import DBConnection
import mysql.connector
from mysql.connector import errorcode
from faker import Faker
import random
from datetime import datetime, timedelta


# def EliminarTablaUsuarios():
#     connection = DBConnection()
#     if connection is None:
#         return {"status": 500, "message": "Error al conectar con la base de datos"}
    
#     try:
#         cursor = connection.cursor()

#         # Desactivar restricciones de clave externa temporalmente
#         cursor.execute("SET foreign_key_checks = 0")
#         connection.commit()

#         # Realizar cambios en la estructura de la base de datos
#         cursor.execute("DROP TABLE IF EXISTS `LogInventarios`")
#         connection.commit()

#         cursor.execute("""CREATE TABLE `LogInventarios` (
#                             `IDLog` INT PRIMARY KEY AUTO_INCREMENT,
#                             `IDUsuario` INT,
#                             `TimeStamp` DATE,
#                             `IDMedicina` INT,
#                             `Cantidad` INT,
#                             FOREIGN KEY (`IDMedicina`) REFERENCES `Medicinas`(`IDMedicina`),
#                             FOREIGN KEY (`IDUsuario`) REFERENCES `Usuarios`(`IDUsuario`)
#                             )ENGINE=InnoDB DEFAULT CHARSET=latin1;
#                         """)
#         connection.commit()



#         # Eliminar la tabla 'Usuarios' (ahora sin restricciones de clave externa)
#         cursor.execute("DROP TABLE IF EXISTS `Usuarios`")
#         connection.commit()

#         # Crear la nueva tabla 'Usuarios'
#         cursor.execute("""CREATE TABLE `Usuarios` (
#                             `IDUsuario` INT PRIMARY KEY AUTO_INCREMENT,
#                             `Username` VARCHAR(100),
#                             `Password` VARCHAR(100),
#                             `TipoAcceso` ENUM('Almacen','Proveedor','Ejecutivo','Compras', 'Medico', 'Paciente', 'Administrador')
#                             )ENGINE=InnoDB DEFAULT CHARSET=latin1;
#                         """)
#         connection.commit()

#         # Activar restricciones de clave externa
#         cursor.execute("SET foreign_key_checks = 1")

#         return {"status": 200, "message": "Tablas eliminadas y creadas correctamente"}

#     except mysql.connector.Error as err:
#         print("Error al editar la base de datos: {}".format(err))
#         return {"status": 500, "message": "Error al editar la base de datos"}
    
#     finally:
#         if 'connection' in locals() and connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("Conexión cerrada")

def EditarTablaPaciente():

    # función para agregar la columna de IDUsuario a la tabla de pacientes como llave foránea de la tabla de usuarios
    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()

        # Desactivar restricciones de clave externa temporalmente
        cursor.execute("SET foreign_key_checks = 0")
        connection.commit()



        cursor.execute("ALTER TABLE Polizas ADD COLUMN IDPaciente INT")
        connection.commit()

        cursor.execute("ALTER TABLE Polizas ADD FOREIGN KEY (IDPaciente) REFERENCES Pacientes(IDPaciente)")
        connection.commit()

        # Activar restricciones de clave externa
        cursor.execute("SET foreign_key_checks = 1")

        return {"status": 200, "message": "Columna agregada correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al editar la base de datos: {}".format(err))
        return {"status": 500, "message": "Error al editar la base de datos"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EditarTablaDoctores():

    #función para agregar la columna de IDUsuario a la tabla de doctores como llave foránea de la tabla de usuarios

    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()

        # Desactivar restricciones de clave externa temporalmente
        cursor.execute("SET foreign_key_checks = 0")
        connection.commit()

        # Realizar cambios en la estructura de la base de datos
        cursor.execute("ALTER TABLE Doctores ADD COLUMN IDUsuario INT")
        connection.commit()

        cursor.execute("ALTER TABLE Doctores ADD FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)")
        connection.commit()

        # Activar restricciones de clave externa
        cursor.execute("SET foreign_key_checks = 1")

        return {"status": 200, "message": "Columna agregada correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al editar la base de datos: {}".format(err))
        return {"status": 500, "message": "Error al editar la base de datos"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def EditarTablaProovedores():
    #función para agregar la columna de IDUsuario a la tabla de proveedores como llave foránea de la tabla de usuarios

    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()

        # Desactivar restricciones de clave externa temporalmente
        cursor.execute("SET foreign_key_checks = 0")
        connection.commit()

        # Realizar cambios en la estructura de la base de datos
        cursor.execute("ALTER TABLE Proveedores ADD COLUMN IDUsuario INT")
        connection.commit()

        cursor.execute("ALTER TABLE Proveedores ADD FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)")
        connection.commit()

        # Activar restricciones de clave externa
        cursor.execute("SET foreign_key_checks = 1")

        return {"status": 200, "message": "Columna agregada correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al editar la base de datos: {}".format(err))
        return {"status": 500, "message": "Error al editar la base de datos"}
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")


def LlenasTabla():
    #función para llenar la columna de IDUsuario a la tabla de doctores como llave foránea de la tabla de usuarios

    connection = DBConnection()
    if connection is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    try:
        cursor = connection.cursor()

        # Desactivar restricciones de clave externa temporalmente
        cursor.execute("SET foreign_key_checks = 0")
        connection.commit()

        # Realizar cambios en la estructura de la base de datos
        cursor.execute("INSERT INTO `Polizas` VALUES (101,36,'1983-07-25','Premium',419867.36,'1974-10-13',1.32),(102,83,'2001-03-15','Premium',469812619.35,'1990-12-11',75640.89),(103,19,'2021-02-06','Estandar',9084.3,'2013-09-27',601354.62),(104,42,'1978-08-16','Estandar',240312.4,'1978-02-15',9828.42),(105,70,'2019-08-29','Basica',7328.98,'1993-07-07',34581.13),(106,58,'2000-01-25','Premium',23706.05,'1970-03-14',555770.71),(107,94,'2017-07-11','Premium',9909.01,'2009-08-11',0),(108,2,'1982-04-28','Basica',77826324.83,'2013-02-09',0),(109,33,'1979-06-24','Estandar',1944.78,'1986-12-16',5167.74),(110,77,'2009-09-28','Basica',15545835.99,'1984-12-09',11191458.33),(111,10,'2022-01-01','Estandar',2449.65,'2008-10-02',49163865.08),(112,100,'1986-09-21','Basica',74651035.71,'2003-11-29',396298.69),(113,83,'2006-09-12','Basica',1149662.38,'2019-11-07',26.19),(114,33,'1997-04-16','Basica',2074.38,'1996-01-20',27.66),(115,32,'1996-06-03','Estandar',5738.95,'1995-03-05',110089.85),(116,18,'2008-03-06','Premium',1751.43,'1993-02-28',0.06),(117,29,'1978-02-14','Estandar',5503864.19,'1990-03-10',430505.59),(118,36,'1979-02-24','Premium',914384925.01,'1971-10-09',46.93),(119,33,'1988-06-04','Premium',3126.84,'1975-05-04',41567999.55),(120,48,'2012-01-18','Basica',11225.17,'2019-06-05',471.76),(121,75,'2013-01-12','Estandar',248626868.48,'1972-04-28',1072.36),(122,95,'1978-09-12','Premium',9588.07,'2010-06-30',315325.04),(123,67,'1984-09-19','Estandar',80359.5,'2000-08-13',1.92),(124,85,'2003-12-05','Estandar',1953.81,'1988-11-25',50839.53),(125,51,'1997-02-13','Estandar',961.67,'2009-10-17',2.53),(126,19,'1999-10-08','Basica',317679.18,'2016-09-25',3.5),(127,43,'1993-10-07','Estandar',22074377.25,'1998-07-01',1.96),(128,36,'2007-06-15','Basica',13696.25,'1994-04-22',0),(129,48,'2015-08-04','Basica',9680.56,'1994-12-30',5022283.35),(130,38,'1983-05-09','Basica',22636.21,'1971-10-21',1521.31),(131,77,'1977-03-16','Estandar',3113.39,'2000-12-20',188.71),(132,12,'1981-09-16','Basica',8329.77,'2014-09-19',0),(133,31,'1970-11-01','Basica',6292794.28,'1982-12-09',5.08),(134,49,'2001-09-15','Premium',122.88,'2012-05-05',5.45),(135,53,'1987-09-17','Estandar',134114.68,'1983-05-16',55577.37),(136,75,'1977-02-10','Premium',3091.39,'1971-08-06',5343494.06),(137,12,'1996-07-21','Basica',31204.7,'2001-07-31',392.15),(138,15,'2010-06-04','Estandar',18287.13,'1973-02-14',10918.72),(139,27,'2002-02-02','Estandar',411940392.58,'2009-01-02',61204232.9),(140,99,'1975-07-01','Estandar',9195.69,'1977-01-03',74.54),(141,43,'2008-07-12','Basica',15420.83,'2008-06-02',569386.26),(142,20,'2005-03-21','Basica',75561047.61,'2023-11-17',8446660.05),(143,78,'1985-08-08','Premium',6860.35,'2000-12-02',0.21),(144,91,'2019-01-22','Premium',1566.37,'1972-07-07',346316.91),(145,7,'1983-12-04','Premium',16682978.75,'2000-10-20',231351.16),(146,83,'1992-08-15','Basica',21112.41,'2006-12-26',12284911.06),(147,85,'1997-08-12','Premium',67644970.14,'1975-05-28',2.96),(148,29,'1982-10-05','Premium',3448.44,'2005-11-24',5238247.32),(149,35,'1971-12-26','Premium',9151597.42,'1992-12-02',42984365.43),(150,35,'1989-11-10','Basica',3378052.83,'2021-09-02',15470557.48),(151,4,'1996-08-08','Estandar',2898.45,'2010-01-27',3264955.97),(152,86,'2002-07-01','Estandar',2181.61,'1992-05-23',0.45),(153,73,'1983-08-14','Estandar',2693.02,'1974-02-16',21865.75),(154,84,'2012-05-12','Basica',7206.87,'1999-07-23',72.99),(155,69,'2013-05-07','Premium',7631369.14,'1990-09-20',382148.77),(156,18,'1987-07-21','Estandar',8123.41,'1978-05-31',160.49),(157,36,'1993-04-04','Estandar',2089.06,'1998-10-14',3197.17),(159,38,'2006-10-23','Basica',7585.2,'1996-01-25',1.33),(160,97,'2018-12-13','Premium',36399379.94,'2020-10-01',0.99),(161,100,'2017-04-11','Estandar',15023.79,'2023-02-09',6980755.92),(162,44,'1989-03-31','Estandar',6360285.19,'2000-12-21',439.62),(163,43,'2004-02-08','Premium',914036.7,'2013-07-02',19.51),(164,15,'1982-08-15','Premium',2341.24,'2001-10-13',387.63),(165,38,'2016-11-19','Estandar',57914.27,'2007-07-15',368043045.02),(166,81,'2013-03-20','Premium',46476633.45,'1971-10-29',48.67),(167,24,'2002-02-16','Estandar',265491491.95,'2009-10-19',405273318.22),(168,82,'1978-11-11','Premium',155376318.92,'1994-05-08',952.48),(169,91,'1979-06-16','Basica',479.9,'1984-07-14',0),(170,61,'2011-05-27','Premium',9930.13,'1990-10-06',229.81),(171,94,'1978-01-31','Premium',220541143.03,'1973-04-06',56381.19),(172,65,'1998-04-10','Premium',417388.78,'1975-09-14',1090.1),(173,77,'2023-07-05','Premium',123536043.12,'2016-01-20',27398315.96),(174,70,'1999-11-28','Basica',109073540.62,'1970-11-26',27441831.4),(175,24,'2016-10-19','Basica',7936.31,'2002-03-19',0.38),(176,82,'1977-07-27','Premium',47906039.93,'1989-07-14',616399.43),(177,12,'2022-09-13','Premium',4890.12,'1993-10-29',742005.04),(178,4,'2011-09-18','Basica',78227.75,'2001-03-02',4.68),(179,92,'1979-01-09','Basica',1782710.78,'1976-02-06',27.76),(180,59,'1975-10-16','Premium',61997.82,'2005-11-17',33221227.85),(181,36,'1979-11-20','Estandar',411344249.98,'2019-04-10',166192314.46),(182,77,'1998-10-28','Basica',8805.42,'2005-04-23',50.07),(183,19,'2012-02-05','Basica',10062.44,'1973-02-01',97.23),(184,17,'1978-07-12','Estandar',65755.91,'2014-01-30',9855886.86),(185,59,'2010-10-25','Premium',34920.73,'1995-06-10',8569748.78),(186,12,'2008-09-28','Basica',7555.04,'2012-11-09',319544763.58),(187,99,'1976-03-07','Estandar',111924.18,'1984-11-26',12337596.07),(188,43,'2023-06-01','Estandar',7911.33,'2023-09-22',0),(189,39,'1997-01-02','Premium',4129765.62,'1978-04-03',0),(190,29,'1973-06-22','Basica',7977.26,'2009-07-09',12639.27),(191,66,'1993-02-09','Basica',2404.14,'2018-03-18',214.61),(192,64,'2013-12-24','Estandar',421095.26,'1993-11-20',3834.56),(193,41,'1978-01-31','Estandar',42968540.48,'1987-01-10',2674498.82),(194,51,'1986-12-27','Premium',3247.52,'2022-12-16',45903.45),(195,62,'1999-11-14','Premium',7840.42,'1985-02-03',209.4),(196,22,'1990-09-06','Basica',47783.51,'1996-12-21',13.8),(197,45,'1992-09-05','Premium',44050377.81,'2019-12-27',47.22),(198,37,'1983-04-27','Estandar',7657.38,'2001-07-23',26411707.61),(199,65,'2011-05-25','Premium',4701.89,'1998-07-30',35418456.69),(200,10,'2002-10-05','Basica',47312844.42,'1991-05-11',0);")
        connection.commit()

        # Activar restricciones de clave externa
        cursor.execute("SET foreign_key_checks = 1")
        
        return {"status": 200, "message": "Tabla llena correctamente"}
    
    except mysql.connector.Error as err:
        print("Error al editar la base de datos: {}".format(err))
        return {"status": 500, "message": "Error al editar la base de datos"}


def generar_datos_prueba(num_citas):
    try:

        conexion = DBConnection()
        if conexion is None:
            return {"status": 500, "message": "Error al conectar con la base de datos"}
        
        cursor = conexion.cursor()


        # Crear un objeto Faker para generar datos ficticios
        faker = Faker()

        # Lista de tipos de cita y estatus de cita
        tipos_cita = ['Estandar', 'DePrueba']
        estatus_cita = [1,2,3]

        # Obtener la lista de IDs de doctores y pacientes existentes (puedes modificar según tu implementación)
        cursor.execute("SELECT IDDoctor FROM Doctores")
        doctores = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT IDPaciente FROM Pacientes")
        pacientes = [row[0] for row in cursor.fetchall()]

        # Generar datos de prueba
        for _ in range(num_citas):
            id_paciente = random.choice(pacientes)
            id_doctor = random.choice(doctores)
            tipo_cita = random.choice(tipos_cita)
            estatus_cita = random.randint(1,3)  # Usar la lista predefinida
            fecha_cita = faker.date_between(start_date='-30d', end_date='+30d')  # Fecha aleatoria en los últimos 30 días

            # Impresiones para depurar
            print(f"IDPaciente: {id_paciente}, IDDoctor: {id_doctor}, TipoCita: {tipo_cita}, EstatusCita: {estatus_cita}, Fecha: {fecha_cita}")

            # Insertar datos en la tabla
            cursor.execute("INSERT INTO Citas (IDPaciente, IDDoctor, TipoCita, EstatusCita, Fecha) VALUES (%s, %s, %s, %s, %s)",
                        (id_paciente, id_doctor, tipo_cita, estatus_cita, fecha_cita))


        # Confirmar y cerrar la conexión
        conexion.commit()
        cursor.close()
        conexion.close()

        print(f'Se han insertado {num_citas} registros en la tabla Citas.')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Acceso denegado. Verifica las credenciales.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(f"Error: {err}")
    except Exception as e:
        print(f"Error inesperado: {e}")


def LlenarTablaFacturas():
    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener la lista de IDCita existentes en la tabla Citas
    cursor.execute("SELECT IDCita FROM Citas")
    id_citas_existentes = [row[0] for row in cursor.fetchall()]

    for i in range(200):
        idCita = random.choice(id_citas_existentes) if id_citas_existentes else None
        costo = random.randint(100, 10000)

        cursor.execute("INSERT INTO Factura (idCita, Costo) VALUES (%s, %s)",
                        (idCita, costo))
        
    conexion.commit()
    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Facturas.')


def LlenarTablaUsuariosdePacientes():
    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener todos los usuarios de tipo paciente y buscar a qué paciente pertenecen, juntar el nombre y el apellido para formar el username y compararlo con el username de la tabla de usuarios, si coinciden, insertar el IDUsuario en la tabla de pacientes

    cursor.execute("SELECT * from Usuarios where TipoAcceso = 'Paciente'")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT * from Pacientes")
    pacientes = cursor.fetchall()

    for paciente in pacientes:
        for usuario in usuarios:
            if usuario[1] == paciente[1] + paciente[2]:
                cursor.execute("UPDATE Pacientes SET IDUsuario = %s WHERE IDPaciente = %s", (usuario[0], paciente[0]))

    conexion.commit()
    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Facturas.')
        

def LlenarTablaUsuariosdeDoctores():

    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener todos los doctores de la tabla Doctores y crear un usuario para cada uno, juntar su nombre y apellido para crear el username y generar una contraseña aleatoria con faker

    cursor.execute("SELECT * from Doctores")
    doctores = cursor.fetchall()

    for doctor in doctores:
        username = doctor[2] + doctor[3]
        password = Faker().password()
        cursor.execute("INSERT INTO Usuarios (Username, Password, TipoAcceso) VALUES (%s, %s, %s)", (username, password, 'Medico'))

    conexion.commit()

    cursor.execute("SELECT * from Usuarios where TipoAcceso = 'Medico'")
    usuarios = cursor.fetchall()

    for doctor in doctores:
        for usuario in usuarios:
            if usuario[1] == doctor[2] + doctor[3]:
                cursor.execute("UPDATE Doctores SET IDUsuario = %s WHERE IDDoctor = %s", (usuario[0], doctor[0]))

    conexion.commit()

    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Usuarios.')


def LLenarColumnaEmailPacientes():
    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener todos los doctores de la tabla Doctores y crear un usuario para cada uno, juntar su nombre y apellido para crear el username y generar una contraseña aleatoria con faker

    cursor.execute("SELECT * from Pacientes")
    pacientes = cursor.fetchall()

    for paciente in pacientes:
        email = paciente[1] + paciente[2] + '@gmail.com'
        cursor.execute("UPDATE Pacientes SET Email = %s WHERE IDPaciente = %s", (email, paciente[0]))

    conexion.commit()

    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Usuarios.')

def LLenarColumnaInsurancePacientes():
    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener todos los doctores de la tabla Doctores y crear un usuario para cada uno, juntar su nombre y apellido para crear el username y generar una contraseña aleatoria con faker

    cursor.execute("SELECT * from Pacientes")
    pacientes = cursor.fetchall()

    for paciente in pacientes:
        insurance = random.choice(['Si', 'No'])
        cursor.execute("UPDATE Pacientes SET Insurance = %s WHERE IDPaciente = %s", (insurance, paciente[0]))

    conexion.commit()

    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Usuarios.')
    
def LLenarColumnaIDPAcientePolizas():
    conexion = DBConnection()

    if conexion is None:
        return {"status": 500, "message": "Error al conectar con la base de datos"}
    
    cursor = conexion.cursor()

    # Obtener todos los doctores de la tabla Doctores y crear un usuario para cada uno, juntar su nombre y apellido para crear el username y generar una contraseña aleatoria con faker

    cursor.execute("SELECT * from Polizas")
    polizas = cursor.fetchall()

    cursor.execute("SELECT * from Pacientes")
    pacientes = cursor.fetchall()


    for paciente in pacientes:
        cursor.execute("UPDATE Polizas SET IDPaciente = %s WHERE IDPoliza = %s", (paciente[0], poliza[0]))
    cursor.close()

    print(f'Se han insertado 200 registros en la tabla Usuarios.')

def main():
    print(LLenarColumnaIDPAcientePolizas())

if __name__ == "__main__":
    main()
