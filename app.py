from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    infos = []
    con = sqlite3.connect("final.db")
    cur = con.cursor()
    sql = "select * from 'Lower Secondary2' where Total and Rural_Residence and Urban_Residence is not NULL limit 5"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)

    score = []
    num = []
    con = sqlite3.connect("final.db")
    cur = con.cursor()
    sql = "select `Countries and areas`,Total from 'Lower Secondary2' where Total is not null "
    data1 = cur.execute(sql)
    for item in data1:
        score.append(str(item[0]))
        num.append(item[1])
    # print(score)
    # print(num)

    datalist = []
    con = sqlite3.connect("final.db")
    cur = con.cursor()
    sql = "select Female,Male from 'Lower Secondary2' where Female and Male is not null"
    data2 = cur.execute(sql)
    for item in data2:
        datalist.append([item[0],item[1]])

    cur.close()
    con.close()
    return render_template("index.html", infos=infos, num=num, score=score, datalist=datalist)


if __name__ == '__main__':
    app.run()
