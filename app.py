from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db' 
app.config['MYSQL_USER'] = 'test_user'
app.config['MYSQL_PASSWORD'] = '1'
app.config['MYSQL_DB'] = 'my_database'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    cur.close()
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['POST'])
def add_order():
    tracking = request.form['tracking']
    name = request.form['customer']
    address = request.form['address']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO orders (tracking_number, customer_name, address, status) VALUES (%s, %s, %s, %s)",
                (tracking, name, address, status))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_status(id):
    new_status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE orders SET status=%s WHERE id=%s", (new_status, id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_order(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM orders WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
