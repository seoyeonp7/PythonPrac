from flask import Flask
import psycopg2
from flask.globals import request
from flask import Flask, render_template, request
from day11.dao_mem import DaoMem

app = Flask(__name__)

@app.route('/')
@app.route('/mem_list')
def mem_list():
    de = DaoMem()
    list = de.selects()
    return render_template('mem_list.html',list=list)

@app.route('/mem_detail')
def mem_detail():
    de = DaoMem()
    m_id = request.args.get('m_id','')
    mem = de.select(m_id)
    return render_template('mem_detail.html',mem=mem)

@app.route('/mem_edit')
def mem_edit():
    de = DaoMem()
    m_id = request.args.get('m_id','')
    mem = de.select(m_id)
    print("왓다")
    return render_template('mem_edit.html',mem=mem)

@app.route('/mem_edit_act',methods=['POST'])
def mem_edit_act():
    de = DaoMem()
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    
    cnt = de.update(m_id,m_nm,tel,ymd)
    
    return render_template('mem_edit_act.html',cnt=cnt)

@app.route('/mem_add')
def mem_add():
    return render_template('mem_add.html')

@app.route('/mem_add_act',methods=['POST'])
def mem_add_act():
    de = DaoMem()
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    
    cnt = de.insert(m_id, m_nm, tel, ymd)
    
    return render_template('mem_add_act.html',cnt=cnt)

@app.route('/mem_delete',methods=['POST'])
def mem_delete():
    de = DaoMem()
    m_id = request.form['m_id']
    cnt = de.delete(m_id)
    return render_template('mem_delete.html',cnt=cnt)


if __name__ == '__main__':
    app.run(debug=True)

