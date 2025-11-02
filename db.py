import mysql.connector

class Info:
    def __init__(self):
        pass
    def connect(self):
        
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vyshnavi05@@",
            database="mark"
        )
        # Creating a cursor
        
    def insert(self,rollno,name):
        self.connect()
        self.cur= self.con.cursor()
        self.cur.execute("insert into memo values(%s,%s)",(rollno,name,))
        self.con.commit()
        self.cur.close()
        self.con.close()

    def display(self,rollno):
        self.connect()
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM memo where hallticket=%s", (rollno,))
        data = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return data