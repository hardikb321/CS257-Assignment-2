from flask import Flask, render_template, request, redirect, url_for, flash
import MySQLdb

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="user_login_registration")
cursor = db.cursor()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        mobile_number = request.form['mobile_number']
        password = request.form['password']

        
        try:
            cursor.execute("INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)",
                           (user_id, mobile_number, password))
            db.commit()
            flash("Registration successful! You can now log in.")
            return redirect(url_for('login'))
        except MySQLdb.Error as e:
            db.rollback()
            flash("Error during registration. Try again.")
    return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']

    
        cursor.execute("SELECT * FROM users WHERE user_id = %s AND password = %s", (user_id, password))
        user = cursor.fetchone()

        if user:
            return render_template('welcome.html')
        else:
            flash("Invalid credentials, please try again.")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
