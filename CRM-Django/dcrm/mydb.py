import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user= 'root',
    passwd = 'Vaish@2002'

)

#prepare cursor object
cursorObject =dataBase.cursor()

#create datbase
cursorObject.execute("CREATE DATABASE crm_database")

print("All done!")