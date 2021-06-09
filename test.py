from flask import Flask, render_template
import pyodbc
server = 'adbservertest.database.windows.net'
database = 'adbdatabasetest'
username = 'adblogin'
password = 'A1@345678'   
driver= '{ODBC Driver 17 for SQL Server}'
app = Flask(__name__)

@app.route('/')
def home():
       return render_template('main.html')


@app.route('/display')
def display():
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Picture  FROM people WHERE Name = 'Tavo'")
            row = cursor.fetchone()
            while row:
                print (str(row[0]))
               
                break
            return render_template('page2.html',filename=row[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055)