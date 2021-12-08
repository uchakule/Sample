import pymysql

class DBconnections:
    def __init__(self,db_config):
        self.database = db_config.get("db_settings","").get("database","")
        self.user = db_config.get("db_settings","").get("user","")
        self.password = db_config.get("db_settings","").get("password","")
        self.host = db_config.get("db_settings","").get("host","")
        self.port = db_config.get("db_settings","").get("port","")
        self.connection = pymysql.connect(host=self.host, user=self.user,password= self.password, db=self.database)
   
    def get_connection(self):
        return self.connection        