import pymysql, time, os, sys
from .config import *

class Mysql():
    """This is a mysql database class."""

    def __init__(self):
        self.db = pymysql.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWORD, db = DB_NAME, port = DB_PORT, charset = DB_CHARSET)
        self.cursor = self.db.cursor()

    def insert(self, sql, data = ()):
        """insert data"""
        return self.execute(1, sql, data)
	
    def update(self, sql, data = ()):
        """update data"""
        return self.execute(2, sql, data)

    def delete(self, sql, data = ()):
        """delete data"""
        return self.execute(3, sql, data)

    def execute(self, operation, sql, data = ()):
        """execute sql"""
        try:
            self.cursor.execute(sql, data)
            if operation == 1:
                insertId = int(self.cursor.lastrowid)
            self.db.commit()
            if operation == 1:
                return insertId
            return True
        except:
            print('ERROR SQL : ', sql, data)
            self.errorLog(sql, data)
            if operation == 1:
                return 0
            return False

    def getRow(self, sql, data = ()):
        """get a row of data"""
        return self.select(1, sql, data)

    def getAll(self, sql, data = ()):
        """get multiple rows of data"""
        return self.select(2, sql, data)

    def getOne(self, sql, data = ()):
        """get a column of data in a row"""
        return self.select(3, sql, data)

    def getCol(self, sql, data = ()):
        """get a column of data"""
        return self.select(4, sql, data)

    def select(self, operation, sql, data):
        """processing query operations"""
        result = ''
        try:
            self.cursor.execute(sql, data)
            if operation == 1:
                data = self.cursor.fetchone()
                if data != None:
                    result = data
            elif operation == 2:
                data = self.cursor.fetchall()
                if len(data) > 0:
                    result = data
            elif operation == 3:
                data = self.cursor.fetchone()
                if data != None:
                    result = data[0]
            else:
                data = self.cursor.fetchall()
                if len(data) > 0:
                    result = []
                    for item in data:
                        result.append(item[0])
        except:
            print('ERROR SQL : ', sql, data)
            self.errorLog(sql, data)
		
        return result

    def errorLog(self, sql, data):
        """sql error log"""
        localTime = time.localtime()
        month = time.strftime('%Y%m', localTime)
        day = time.strftime('%Y%m%d', localTime)
        strTime = time.strftime('%Y-%m-%d %H:%M:%S', localTime)
        if 'LOG_DIR' in globals() and LOG_DIR != "":
            if LOG_DIR[-1] == "/":
                path = LOG_DIR + "sqlErrorLog/" + month
            else:
                path = LOG_DIR + "/sqlErrorLog/" + month
            if os.path.exists(path) == False:
                os.makedirs(path)
            fileName = path + "/" + day + ".log"
            f = open(fileName, 'a+')
            content = strTime + " | " + sql + " | " + ','.join(data) + "\n"
            f.write(content)
            f.close()
        else:
            print('file directory error')
