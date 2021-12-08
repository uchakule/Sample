from flask import Flask,request
from libs.core.Student import Student
import json

from libs.tables.DBconnections import DBconnections

db_config = json.load(open('./config/config.json','r'))
dbops = DBconnections(db_config)

app = Flask(__name__)

@app.route('/')
def get_all_records():
    query = request.args['filter']
    student = Student(dbops)
    results = student.payload(query)
    return results

if __name__ == '__main__':
    app.run(debug=True)
