from flask import Flask, render_template, request, redirect, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="data_pawdoct"
)

@app.route('/')
def homepage():
    if 'username' in session:
        return render_template('homepage.html')
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  
        
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            db.commit()
            return redirect('/login')
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Registration failed. Please try again."
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (identifier, identifier))
        user = cursor.fetchone()

        if user:
            stored_password_hash = user[3] 
            print(f'Stored password hash: {stored_password_hash}')  
            print(f'Input password: {password}')  

            
            if check_password_hash(stored_password_hash, password):
                session['username'] = user[2]
                return redirect('/')  
            else:
                print('Password does not match') 
        else:
            print('User not found') 

        return 'Login Failed'

    return render_template('login.html')


@app.route('/diagnose', methods=['GET', 'POST'])
def diagnose():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms')

        cursor = db.cursor()
        disease_result = {}

        for symptom in symptoms:
            cursor.execute("SELECT disease, probability FROM diagnosis WHERE symptom = %s", (symptom,))
            result = cursor.fetchone()
            if result:
                disease, prob = result
                if disease in disease_result:
                    disease_result[disease] += prob
                else:
                    disease_result[disease] = prob

        if disease_result:
            disease_diagnosed = max(disease_result, key=disease_result.get)
            probability = disease_result[disease_diagnosed]
        else:
            disease_diagnosed = "Unknown"
            probability = 0

        return f'Kemungkinan penyakit: {disease_diagnosed} dengan kemungkinan {probability}%'

    return render_template('diagnosa.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
