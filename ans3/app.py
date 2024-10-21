from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'password'  
app.config['MYSQL_DB'] = 'user_registration'

mysql = MySQL(app)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    user_id = request.form['userId']
    mobile_number = request.form['mobileNumber']
    password = request.form['password']

    
    if len(user_id) < 5:
        return render_template('register.html', message="User ID must be at least 5 characters long.")
    elif not re.match(r'^[0-9]{10}$', mobile_number):
        return render_template('register.html', message="Mobile number must be 10 digits.")
    elif len(password) < 6:
        return render_template('register.html', message="Password must be at least 6 characters long.")
    
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)', (user_id, mobile_number, password))
    mysql.connection.commit()
    cursor.close()

    return render_template('register.html', message="Registration successful!")

if __name__ == '__main__':
    app.run(debug=True)
