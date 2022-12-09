from flask import Flask
from flask.globals import request
from flask import Flask, render_template
from flask.json import jsonify
from day14.dao_teacher import DaoTeacher

app = Flask(__name__)

@app.route('/')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/ajax_teacher_list', methods=['POST'])
def ajax_teacher_list():
    data = request.get_json()
    dt = DaoTeacher()
    list = dt.selects()
    return jsonify(list=list)

@app.route('/ajax_teacher_one', methods=['POST'])
def ajax_teacher_one():
    dict = request.get_json()
    dt = DaoTeacher()
    teacher = dt.select(dict['t_id'])
    print(teacher)
    return jsonify(teacher=teacher)

@app.route('/ajax_teacher_add', methods=['POST'])
def ajax_teacher_add():
    dict = request.get_json()
    dt = DaoTeacher()
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr = dict['addr']
    cnt = dt.insert(t_name,mobile,addr)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_teacher_modify', methods=['POST'])
def ajax_teacher_modify():
    dict = request.get_json()
    dt = DaoTeacher()
    t_id = dict['t_id']
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr = dict['addr']
    cnt = dt.update(t_id,t_name,mobile,addr)
    print(cnt)
    return jsonify(cnt=cnt)

@app.route('/ajax_teacher_delete', methods=['POST'])
def ajax_teacher_delete():
    dict = request.get_json()
    dt = DaoTeacher()
    cnt = dt.delete(dict['t_id'])
    print(cnt)
    return jsonify(cnt=cnt)


if __name__ == '__main__':
    app.run(debug=True)

