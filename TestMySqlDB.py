SQLALCHEMY_DATABASE_URI = "mysql+pymysql://azure:6#vWHD_$@127.0.0.1:56080/localdb"
print(SQLALCHEMY_DATABASE_URI)

# Open database connection
import pymysql as PyMySQL

db = PyMySQL.connect("localhost","Adam","adam","mydb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()

