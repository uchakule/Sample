import json
from libs.tables.DBconnections import DBconnections
from flask import jsonify

class Student:
    def __init__(self,dbops):
        self.connection = dbops.get_connection()

    def get_data(self,query):
        cursor = self.connection.cursor()
        sql = """SELECT * FROM student
                 WHERE (UPPER(student_name) LIKE UPPER('%{}%') OR
                 UPPER(major) LIKE UPPER('%{}%') OR
                 UPPER(city) LIKE UPPER('%{}%'))
                 ORDER BY student_name ASC
              """.format(query,query,query)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    
    def payload(self,query):
        data_dict = []
        results = Student.get_data(self,query)
        for data in results :
            datap ={
                'id': data[0],
                'name':data[1],
                'stream':data[2],
                'city':data[3]
            }
            data_dict.append(datap)
        return jsonify(data_dict)   

      