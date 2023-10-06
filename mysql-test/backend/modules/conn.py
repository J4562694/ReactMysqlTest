from typing import Any
from mysql import connector
from config import Sqlstuff

def getConn() -> Any:
    return connector.connect(
        host=Sqlstuff.host,
        user=Sqlstuff.user,
        password=Sqlstuff.password,
        database=Sqlstuff.database
    )

def createUsers(sqlQuery) -> Any:
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sqlQuery)
    result = cursor.fetchall()
    conn.close()
    return result