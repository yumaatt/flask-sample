from flask import Flask, request, render_template, jsonify
# from flask import escape
import pymysql
import os


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False

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

    return jsonify({
        'status':'OK',
        'members':members
        })
    # return render_template('hello.html', title='flask test', members=members)


@app.route('/hello2')
def hello2():
    name = "Hello"
    return name


@app.route('/hello3/<name>')
def hello3(name=None):
    return render_template('hello2.html', title='flask test', name=name)


@app.route('/hello4')
def hello4():
    name = request.args.get('name')
    return render_template('hello2.html', title='flask test', name=name)


@app.route('/hello5', methods=['POST'])
def hello5():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return render_template('hello2.html', title='flask test', name=name)


@app.route('/hello6')
def hello6():
    data = [
        {"name":"山田"},
        {"age":30}
    ]
    return jsonify({
            'status':'OK',
            'data':data
        })


if __name__ == "__main__":
    app.run(debug=True)
