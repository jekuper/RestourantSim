from BotConfigs import *
from datetime import datetime
import MySQLdb
from BotLocalization import *

def Connect():
    conn = MySQLdb.connect( host=HOSTNAME, port=PORT, user=USERNAME, passwd=PASSWORD, db=DATABASE_NAME)
    return conn
def update_user_settings(user_id: int, language: str):
    dbConn = Connect()
    dbCursor = dbConn.cursor()
    params = [language, user_id]
    command = "UPDATE `user_settings` SET `language`=%s WHERE `user_id`=%s"

    dbCursor.execute(command, params)
    dbConn.commit()
    dbConn.close()

def get_user_language(user_id: int):
    dbConn = Connect()
    dbCursor = dbConn.cursor()
    params = [user_id]
    command = "SELECT language FROM `user_settings` WHERE `user_id`=%s"

    dbCursor.execute(command, params)
    myresult = dbCursor.fetchall()
    dbConn.close()
    if len(myresult) == 0:
        return None
    return myresult[0][0]

def insert_new_user(user_id: int) -> bool:
    dbConn = Connect()
    dbCursor = dbConn.cursor()
    params = [user_id]
    command = "SELECT * FROM `user_settings` WHERE `user_id`=%s"

    dbCursor.execute(command, params)
    myresult = dbCursor.fetchall()
    if len(myresult) == 0:
        dbCursor.execute("INSERT INTO `user_settings`(`user_id`, `language`) VALUES (%s,%s)", [user_id, LOCALIZATIONS[0]])
        dbCursor.execute("INSERT INTO `restourants`(`user_id`, `name`) VALUES (%s,%s)", [user_id, "no_name"])
        dbConn.commit()
    dbConn.close()

    if len(myresult) == 0:
        return True
    return False

def set_restourant_name(user_id: int, name: str):
    dbConn = Connect()
    dbCursor = dbConn.cursor()
    dbCursor.execute("UPDATE `restourants` SET `name`=%s WHERE `user_id`=%s", [name, user_id])
    dbConn.commit()
