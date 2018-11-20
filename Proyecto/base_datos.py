import sqlite3

def Database():
    global conn, cursor
    conn = sqlite3.connect("proyecto.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `usuarios` (no_registro INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, correo TEXT, contraseña TEXT)")       
    cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = 'ECFM' AND `contraseña` = 'ECFM'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `usuarios` (correo, contraseña) VALUES('ECFM', 'ECFM')")
        conn.commit()

