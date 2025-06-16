from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection Config

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@Hasan123',
    database = 'stockDB'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stocksdata LIMIT 5;')
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    return render_template('home.html',data=data,columns=columns)

if __name__ == '__main__':
    app.run(debug=True)