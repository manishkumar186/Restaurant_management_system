from pymysql import  *
class connectionfile:
    def connect(self):
        conn = connect("ressonu.db.7623447.73f.hostedresource.net", "ressonu", "VMMeducation@123", "ressonu")
        return conn