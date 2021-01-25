from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Tariff_Plan_Management'

mysql = MySQL(app)

@app.route('/')
def Index():
    # if session.get('customer'):
    #     return redirect(url_for('Customer'))

    return render_template('login.html',title="Login")

@app.route("/",methods=['POST'])
def userAuthenticate():
    username = request.form['username']
    password = request.form['password']
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM ad_login WHERE admin_login='" + username + "' and admin_pass='" + password + "'")
    data = cur.fetchone()
    if data is None:    
        cur.execute("SELECT * FROM cust_login WHERE customer_login='" + username + "' and customer_pass='" + password + "'")
        data = cur.fetchone()
        if data is None:
            flash("Please enter correct credentials","error")
            return render_template('login.html',title="Login")
        else:
            flash(f"{username.title()}, you are logged in successfully","success")
            session['customer'] = username
            return redirect(url_for('Customer'))
    else:
        flash(f"{username.title()} (admin), you logged in successfully","success")
        session['admin']=username
        return redirect(url_for('Admin'))

    return render_template('login.html',title="Login")

@app.route('/customer')
def Customer():
    if not session.get('customer'):
        return render_template('login.html',title="Login")
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM Plan")
    data = cur.fetchall()
    cur.close()
    return render_template('customer.html',title="Customer Portal" , Plan=data, user=session.get('customer'))



@app.route('/admin')
def Admin():
    if not session.get('admin'):
        return render_template('login.html', title="Admin Login")
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM Plan")
    data = cur.fetchall()
    cur.close()

    return render_template('admin.html',title="Admin Portal" , Plan=data , user=session.get('admin'))



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully","success")
        plan_name = request.form['plan_name']
        plan_type = request.form['plan_type']
        tariff = request.form['tariff']
        validity = request.form['validity']
        rental = request.form['rental']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Plan (plan_name, plan_type, tariff, validity, rental) VALUES (%s, %s, %s, %s, %s)", (plan_name, plan_type, tariff, validity, rental))
        mysql.connection.commit()
        return redirect(url_for('Admin'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully","success")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Plan WHERE plan_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Admin'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        plan_name = request.form['plan_name']
        plan_type = request.form['plan_type']
        tariff = request.form['tariff']
        validity = request.form['validity']
        rental = request.form['rental']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE Plan
               SET plan_name=%s, plan_type=%s, tariff=%s, validity=%s, rental=%s
               WHERE plan_id=%s
            """, (plan_name, plan_type, tariff, validity, rental, id_data))
        flash("Data Updated Successfully","success")
        mysql.connection.commit()
        return redirect(url_for('Admin'))

@app.route("/logout")
def logout():
    session['customer']=False
    session['admin']=False
    flash("You are logged out successfully","success")
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
