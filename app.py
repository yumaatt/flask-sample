from flask import Flask, request, render_template
# from flask import escape
import pymysql
import os


app = Flask(__name__)


@app.route('/')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    # return render_template('hello.html', title='flask test', name=name)
    mysql_pass = os.environ['MYSQL_PASS']
    db = pymysql.connect(
            host='localhost',
            user='testuser',
            password=mysql_pass,
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )

    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members)


@app.route('/hello')
def good():
    name = "Hello"
    return name


if __name__ == "__main__":
    app.run(debug=True)
