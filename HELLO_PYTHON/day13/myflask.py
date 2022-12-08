from flask import Flask
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day13.dao_student import DaoStudent

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    ds = DaoStudent()
    list = ds.selects()
    return jsonify(list=list)
    
@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    dict = request.get_json()
    ds = DaoStudent()
    emp = ds.select(dict['s_id'])
    print(emp)
    return jsonify(emp=emp)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    dict = request.get_json()
    ds = DaoStudent()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    cnt = ds.insert(s_id,s_name,mobile,address)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_modify', methods=['POST'])
def ajax_modify():
    dict = request.get_json()
    ds = DaoStudent()
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    address = dict['address']
    cnt = ds.update(s_id,s_name,mobile,address)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    dict = request.get_json()
    ds = DaoStudent()
    cnt = ds.delete(dict['s_id'])
    print(cnt)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)

