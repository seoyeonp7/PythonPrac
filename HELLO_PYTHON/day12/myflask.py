from flask import Flask
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day12.dao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    de = DaoEmp()
    list = de.selects()
    return jsonify(list=list)
    
@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    de = DaoEmp()
    emp = de.select(dict['e_id'])
    print(emp)
    return jsonify(emp=emp)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    de = DaoEmp()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    cnt = de.insert(e_id,e_name,sex,addr)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_modify', methods=['POST'])
def ajax_modify():
    dict = request.get_json()
    de = DaoEmp()
    e_id = dict['e_id']
    e_name = dict['e_name']
    sex = dict['sex']
    addr = dict['addr']
    cnt = de.update(e_id,e_name,sex,addr)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    de = DaoEmp()
    cnt = de.delete(dict['e_id'])
    print(cnt)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)

