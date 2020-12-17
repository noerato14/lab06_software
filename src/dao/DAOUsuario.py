import pymysql

class DAOUsuario:
    def connect(self):
        return pymysql.connect("localhost","root","","db_poo" )

    def read(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by nombre asc")
            else:
                cursor.execute("SELECT * FROM usuario where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(codigo,nombre,username,clave,tipo) VALUES(%s, %s, %s, %s, %s)", (data['codigo'],data['nombre'],data['username'],data['clave'],data['tipo'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set codigo = %s, nombre = %s, username = %s , clave = %s , tipo = %s where id = %s", (data['codigo'],data['nombre'],data['username'],data['clave'],data['tipo'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM usuario where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
