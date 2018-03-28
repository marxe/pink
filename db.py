import MySQLdb
from config.database import config

class db:
    connection = {};
    table = ''
    where = ''
    def __init__(self, table):
        self.table = table
        try:
            #** if dict to args, * list to args
            if not self.connection:
                self.connection = MySQLdb.connect(**config)
        except:
            print("Can't connect to database")
    def connect(self):
        return self.connection
    def insert(self,data):
        last=''
        success = False
        try:
            cursor = self.connection.cursor()
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = """INSERT INTO `%s` (%s) VALUES (%s)"""% (self.table,columns,placeholders)
            cursor.execute(sql, data.values())
            last = self.connection.insert_id()
            self.connection.commit()
            success = True
        except self.connection.Error as e:
            self.connection.rollback()
            success = False
            print(e)

        return {
            'id': last,
            'success': success
        }
    def where(self,data):
        where = ''
        for column in data:
            where += "%s'%s' " % (column,data[column])

        self.where = where

    def select(self,columns):
        list=[]
        success = False
        columns = ', '.join(columns) if len(columns)>0 else '*'
        try:
            cursor = self.connection.cursor(cursorclass = MySQLdb.cursors.DictCursor)
            sql = """SELECT %s FROM %s WHERE %s"""% (columns, self.table, self.where)
            cursor.execute(sql)
            data = cursor.fetchall()
            for cur in data:
                list.append(cur)
            self.connection.commit()
            success = True
        except self.connection.Error as e:
            self.connection.rollback()
            success = False
            print(e)
        return {
            'data': list,
            'success': success
        }