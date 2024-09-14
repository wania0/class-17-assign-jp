import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password="admin", # empty password
        db='assignment_db',
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("db connected")
    return conn
    

def disconnect(conn):
  conn.close()

if __name__ == "__main__":
    mysqlconnect()