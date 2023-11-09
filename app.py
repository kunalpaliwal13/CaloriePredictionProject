from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = 'Calorie.db'
app.secret_key = 'TH15_1S_@_S3CR3T_K3Y'


@app.route('/login',methods=("GET","POST"))
def login():
    if request.method=="POST":
        login_id=request.form['userid']
        passwd = request.form['password']
        login_conn = sqlite3.connect(app.config['DATABASE'])
        cur=login_conn.cursor()
        cur.execute('SELECT password,code FROM users WHERE username = ? password = ?', (login_id,passwd))
        result = cur.fetchone()
        login_conn.close()
        if result:
            print(result)
            session['userid'] = request.form['userid']
            session['name'] = request.form['name']
            session['age'] = request.form['age']
            session['height'] = request.form['height']
            session['gender'] = request.form['gender']
            return redirect(url_for('home'))
        else:
            print("Wrong")
            return render_template('login.html',message="Wrong Id or Password")

    return render_template('login.html')

@app.route('/register.html',methods=("GET","POST"))
def register():
    if request.method=="POST":
        user_id=request.form['userid']
        passwd = request.form['password']
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        gender = request.form['gender']

        register_conn = sqlite3.connect(app.config['DATABASE'])
        register_cur=register_conn.cursor()
        register_cur.execute('SELECT userid FROM users WHERE userid = ?', (user_id,))
        result = register_cur.fetchone()
        if result:
            return render_template('register.html',message="User already exists")
        else:
            register_cur.execute('insert into users values(?,?,?,?,?)',(user_id,passwd,name,age,height,gender))
            register_conn.commit()
            session['userid'] = request.form['userid']
            session['name'] = request.form['name']
            session['age'] = request.form['age']
            session['height'] = request.form['height']
            session['gender'] = request.form['gender']
            return redirect(url_for('home'))
        
@app.route('/home.html',methods=("GET","POST"))
def home():
    if request.method=="POST":
        gender_text=request.form['gender']
        Gender = 0 if gender_text=='Male' else 1
        Age = float(request.form['age'])
        Height = float(request.form['height'])
        Duration=float(request.form['duration'])
        Heart_Rate = float(request.form['heart_rate'])
        Body_Temp = float(request.form['temperature'])
        date=os.date.today()
        model=load_model('model.h5')
        result = model.predict([[Gender,Age,Height,Duration,Heart_Rate,Body_Temp]])
        session['calories'] = result
        exercise_conn = sqlite3.connect(app.config['DATABASE'])
        exercise_cur=exercise_conn.cursor()
        exercise_cur.execute('insert into exercise(exercise_name,userid,duration,date,bpm,temperature,calories) values(?,?,?,?,?,?,?)',(request.form['exercise'],session['userid'],Duration,date,Heart_Rate,Body_Temp,result))
        return render_template('home.html',calories = result)
        

    return render_template('home.html',name = session['name'], age = session['age'], height = session['height'], gender = session['gender'])

@app.route('/dashboard.html',methods=("GET","POST"))
def dashboard():
    pass


if __name__ == '__main__':
    app.run(debug=True)